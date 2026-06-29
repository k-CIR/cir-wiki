from __future__ import annotations

import json
import logging
import re
from contextlib import asynccontextmanager
from dataclasses import asdict
from datetime import datetime, timezone
from pathlib import Path

import secrets

from fastapi import FastAPI, HTTPException, Query
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse

from .config import Settings, get_settings
from .llm import AzureWikiChatClient
from .models import ChatRequest, ChatResponse, FeedbackRequest, HealthResponse, QueryPlan as QueryPlanModel, SourceItem
from .query_planner import QueryPlan, QueryPlanner
from .wiki_index import SearchResult, WikiIndex


logger = logging.getLogger(__name__)

_CITATION_RE = re.compile(r"\[(\d+)\]")
# /home is the only path on Azure App Service that persists across restarts and
# redeployments. Fall back to a local path when running outside Azure.
_AZURE_HOME = Path("/home/ginger")
_LOCAL_FALLBACK = Path(__file__).resolve().parents[1] / "eval"
_FEEDBACK_DIR = _AZURE_HOME if _AZURE_HOME.parent.exists() else _LOCAL_FALLBACK
_FEEDBACK_LOG = _FEEDBACK_DIR / "feedback.jsonl"


def _anchor_text(item: SourceItem) -> str:
    """Return short anchor text for an inline Markdown link."""

    section = " ".join((item.section or "").split())
    if section:
        return section

    anchor = " ".join(item.title.split()[:4])
    return anchor if anchor else "source"


def _clarification_option_url(option: str) -> str | None:
    normalized = re.sub(r"[^a-z0-9]+", " ", option.casefold()).strip()
    known_routes = {
        "natmeg": "/natmeg/",
        "natmeg equipment": "/natmeg/equipment/",
        "natmeg analysis": "/natmeg/MEEG-analysis/",
        "natmeg meeg analysis": "/natmeg/MEEG-analysis/",
        "natmeg preprocessing": "/natmeg/preprocessing/",
        "natmeg acquisition": "/natmeg/data-acquisition/",
        "opm acquisition": "/natmeg/opm-acquisition/",
        "squid acquisition": "/natmeg/squid-acquisition/",
        "spice": "/SPICE/",
        "bmic": "/bmic/",
        "mrc": "/mrc/",
        "server": "/server/",
    }
    return known_routes.get(normalized)


def _cited_sources(results: list[SearchResult], answer: str, cited_indices: list[int]) -> tuple[str, list[SourceItem]]:
    """Return a citation-normalized answer plus sources in rendered citation order."""

    seen: dict[tuple[str, str | None], int] = {}
    citation_map: dict[int, int] = {}
    sources: list[SourceItem] = []

    for citation in cited_indices:
        index = citation - 1
        if index < 0 or index >= len(results):
            continue

        chunk = results[index].chunk
        key = (chunk.url, chunk.section)
        mapped_citation = seen.get(key)
        if mapped_citation is None:
            mapped_citation = len(sources) + 1
            seen[key] = mapped_citation
            sources.append(
                SourceItem(
                    title=chunk.title,
                    url=chunk.url,
                    section=chunk.section,
                    snippet=chunk.snippet,
                )
            )
        citation_map[citation] = mapped_citation

    def _replace_citation(match: re.Match[str]) -> str:
        original = int(match.group(1))
        mapped = citation_map.get(original)
        if mapped is None:
            return ""
        source = sources[mapped - 1]
        return f"[{_anchor_text(source)}]({source.url})"

    normalized_answer = _CITATION_RE.sub(_replace_citation, answer)

    return normalized_answer, sources


def _clarification_answer(options: list[str]) -> str:
    lines = ["The CIR wiki has several relevant categories. Choose one of these to narrow the answer:", ""]
    for option in options:
        url = _clarification_option_url(option)
        lines.append(f"- [{option}]({url})" if url else f"- {option}")
    return "\n".join(lines)


def _plan_to_model(plan: QueryPlan | None) -> QueryPlanModel | None:
    if plan is None:
        return None
    return QueryPlanModel(**asdict(plan))


@asynccontextmanager
async def lifespan(app: FastAPI):
    _FEEDBACK_DIR.mkdir(parents=True, exist_ok=True)
    settings = get_settings()
    wiki_index = WikiIndex.build(
        docs_root=settings.docs_root,
        site_base_url=settings.site_base_url,
        chunk_size=settings.chunk_size,
        chunk_overlap=settings.chunk_overlap,
    )

    app.state.settings = settings
    app.state.wiki_index = wiki_index
    app.state.chat_client = AzureWikiChatClient(settings)
    app.state.query_planner = QueryPlanner(settings)
    yield


app = FastAPI(title="Ginger Chat Backend", version="0.1.0", lifespan=lifespan)

settings = get_settings()
app.add_middleware(
    CORSMiddleware,
    allow_origins=settings.allowed_origins,
    allow_credentials=False,
    allow_methods=["GET", "POST", "OPTIONS"],
    allow_headers=["*"],
)


@app.get("/health", response_model=HealthResponse)
async def health() -> HealthResponse:
    current_settings: Settings = app.state.settings
    chat_client: AzureWikiChatClient = app.state.chat_client
    wiki_index: WikiIndex = app.state.wiki_index

    return HealthResponse(
        status="ok",
        docs_root=str(current_settings.docs_root),
        indexed_chunks=len(wiki_index.chunks),
        azure_configured=chat_client.is_configured,
    )


@app.post("/api/chat", response_model=ChatResponse)
async def chat(request: ChatRequest) -> ChatResponse:
    if not request.message.strip():
        raise HTTPException(status_code=400, detail="Message must not be empty.")

    current_settings: Settings = app.state.settings
    wiki_index: WikiIndex = app.state.wiki_index
    chat_client: AzureWikiChatClient = app.state.chat_client
    query_planner: QueryPlanner = app.state.query_planner

    plan: QueryPlan | None = None
    try:
        plan = query_planner.plan(request.message, request.history)
    except Exception:  # noqa: BLE001
        logger.exception("Planner failed, falling back to direct retrieval")

    if plan and plan.intent == "clarify" and plan.clarification_options:
        return ChatResponse(
            answer=_clarification_answer(plan.clarification_options),
            sources=[],
            grounded=True,
            plan=_plan_to_model(plan),
        )

    retrieval_intent = plan.intent if plan else "definition"
    retrieval_limit = current_settings.retrieval_top_k
    if retrieval_intent in {"inventory", "clarify"}:
        retrieval_limit = 20
    if plan and plan.top_k_override:
        retrieval_limit = plan.top_k_override

    if plan:
        results = wiki_index.search_multi(
            plan.expanded_queries,
            limit=retrieval_limit,
            subtree=plan.subtree,
        )
    else:
        results = wiki_index.search(request.message, limit=current_settings.retrieval_top_k)

    if plan and plan.intent in {"inventory", "clarify"}:
        results = wiki_index.aggregate_by_page(results, page_limit=retrieval_limit)

    if not results:
        return ChatResponse(
            answer="I could not find relevant information for that question in the CIR wiki.",
            sources=[],
            grounded=False,
            plan=_plan_to_model(plan),
        )

    try:
        llm_answer = chat_client.answer(
            question=request.message,
            history=request.history,
            page_context=request.page_context,
            results=results,
            intent=retrieval_intent,
        )
    except Exception as exc:  # noqa: BLE001
        raise HTTPException(status_code=502, detail=f"Azure chat request failed: {exc}") from exc

    answer, sources = _cited_sources(results, llm_answer.answer, llm_answer.cited_indices)

    return ChatResponse(
        answer=answer,
        sources=sources,
        grounded=llm_answer.grounded,
        plan=_plan_to_model(plan),
    )


@app.post("/api/feedback", status_code=204)
async def feedback(request: FeedbackRequest) -> None:
    entry = {
        "ts": datetime.now(timezone.utc).isoformat(),
        "message_id": request.message_id,
        "question": request.question,
        "answer": request.answer,
        "feedback": request.feedback,
        "comment": request.comment or "",
    }
    with _FEEDBACK_LOG.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(entry, ensure_ascii=False) + "\n")


@app.get("/api/feedback/download")
async def feedback_download(token: str = Query(default="")) -> FileResponse:
    """Download the accumulated feedback log as a JSONL file.

    Requires the GINGER_CHAT_DOWNLOAD_TOKEN app setting to be set in Azure.
    Pass the token as a query parameter: ?token=<value>
    """
    current_settings: Settings = app.state.settings
    if not current_settings.download_token:
        raise HTTPException(status_code=503, detail="Download endpoint is not configured (no token set).")
    if not secrets.compare_digest(token, current_settings.download_token):
        raise HTTPException(status_code=401, detail="Invalid token.")
    if not _FEEDBACK_LOG.exists() or _FEEDBACK_LOG.stat().st_size == 0:
        raise HTTPException(status_code=404, detail="No feedback has been recorded yet.")
    return FileResponse(
        path=_FEEDBACK_LOG,
        media_type="application/x-ndjson",
        filename="ginger-feedback.jsonl",
    )
