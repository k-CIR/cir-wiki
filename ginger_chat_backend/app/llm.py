from __future__ import annotations

from dataclasses import dataclass
import re as _re

from openai import OpenAI

from .config import Settings
from .models import ChatMessage, PageContext
from .wiki_index import SearchResult


BASE_SYSTEM_PROMPT = """You are CIRI for the Centre for Imaging Research wiki.

Rules:
- Answer only from the provided CIR wiki context.
- Answer directly and concisely. For non-inventory questions, use at most 3-5 sentences.
- Use inline citations like [1], [2] only for the supplied sources.
- Citations must be bare integers in square brackets only: [1], [2]. Never put words, phrases, titles, or URLs inside brackets.
- Never invent facts, links, or citations.
- Do not add a "Summary:" section or any heading.
- Do not narrate what the sources say before answering. Give the answer directly.
- If retrieved sources genuinely do not cover the question, say so in one sentence.
"""

_CITATION_RE = _re.compile(r"\[(\d+)\]")

INTENT_PROMPTS = {
    "inventory": "Group results by category. Produce a structured list. Cite each category cluster. If sources appear incomplete for a broad question, say the answer is partial and name the categories covered.",
    "procedural": "Give a step-by-step answer. Cite the source for each step.",
    "troubleshooting": "State the likely cause first, then the fix. Cite sources.",
    "definition": "Give a concise direct answer. Cite sources.",
    "comparison": "Use a structured comparison. Cite sources for each item compared.",
}


@dataclass(slots=True)
class LlmAnswer:
    answer: str
    grounded: bool
    cited_indices: list[int]


class AzureWikiChatClient:
    def __init__(self, settings: Settings) -> None:
        self._settings = settings
        self._client = None
        if settings.azure_api_key:
            self._client = OpenAI(
                api_key=settings.azure_api_key,
                base_url=settings.azure_endpoint
            )

    @property
    def is_configured(self) -> bool:
        return self._client is not None

    def answer(
        self,
        question: str,
        history: list[ChatMessage],
        page_context: PageContext | None,
        results: list[SearchResult],
        intent: str,
    ) -> LlmAnswer:
        if not self._client:
            return LlmAnswer(
                answer="The Ginger backend found relevant CIR wiki content, but Azure OpenAI credentials are not configured yet.",
                grounded=False,
                cited_indices=[],
            )

        intent_prompt = INTENT_PROMPTS.get(intent, INTENT_PROMPTS["definition"])
        messages = [{"role": "system", "content": f"{BASE_SYSTEM_PROMPT}\n\nIntent mode:\n- {intent_prompt}"}]
        for message in history[-6:]:
            messages.append({"role": message.role, "content": message.content})

        source_blocks = []
        for index, result in enumerate(results, start=1):
            chunk = result.chunk
            source_blocks.append(
                "\n".join(
                    [
                        f"[{index}] Title: {chunk.title}",
                        f"[{index}] Section: {chunk.section or 'General'}",
                        f"[{index}] Content: {chunk.content[:self._settings.source_char_limit]}",
                    ]
                )
            )

        page_hint = ""
        if page_context and (page_context.title or page_context.url):
            page_hint = (
                "Current page context:\n"
                f"- Title: {page_context.title or 'Unknown'}\n"
                f"- URL: {page_context.url or 'Unknown'}\n\n"
            )

        messages.append(
            {
                "role": "user",
                "content": (
                    f"{page_hint}"
                    "Answer the following question using only the supplied CIR wiki sources. "
                    "If the sources only cover part of a broad question, answer with the covered categories and say the answer is partial.\n\n"
                    f"Question: {question}\n\n"
                    "Sources:\n"
                    f"{'\n\n'.join(source_blocks)}"
                ),
            }
        )

        response = self._client.chat.completions.create(
            model=self._settings.azure_deployment,
            messages=messages,
            max_completion_tokens=2000 if intent == "inventory" else 1200,
            temperature=0.2,
            top_p=1.0,
            response_format={"type": "text"},
        )
        answer = (response.choices[0].message.content or "").strip()
        if not answer:
            answer = "The CIR wiki sources did not produce a usable answer."

        answer_lower = answer.lower()
        grounded = not any(
            marker in answer_lower
            for marker in (
                "does not contain enough information",
                "not found in the retrieved sources",
                "retrieved sources do not cover",
            )
        )
        seen: set[int] = set()
        cited: list[int] = []
        for match in _CITATION_RE.finditer(answer):
            citation = int(match.group(1))
            if citation in seen:
                continue
            seen.add(citation)
            cited.append(citation)

        return LlmAnswer(answer=answer, grounded=grounded, cited_indices=cited)
