from __future__ import annotations

import json
import logging
from dataclasses import dataclass

from openai import OpenAI

from .config import Settings
from .models import ChatMessage


logger = logging.getLogger(__name__)

KNOWN_SUBTREES = [
    "natmeg",
    "natmeg/equipment",
    "natmeg/equipment/stimulus-equipment/audio",
    "natmeg/equipment/stimulus-equipment/visual",
    "natmeg/equipment/stimulus-equipment/other",
    "natmeg/equipment/response-equipment",
    "natmeg/equipment/other",
    "natmeg/MEEG-analysis",
    "natmeg/preprocessing",
    "natmeg/preprocessing/maxfilter",
    "natmeg/opm-acquisition",
    "natmeg/squid-acquisition",
    "natmeg/presentation",
    "natmeg/cerberos",
    "natmeg/bids",
    "natmeg/server",
    "SPICE",
    "bmic",
    "mrc",
    "server",
]

KNOWN_SUBTREE_SET = set(KNOWN_SUBTREES)
KNOWN_INTENTS = {"procedural", "inventory", "definition", "troubleshooting", "comparison", "clarify"}

SITE_MAP = "\n".join(f"- {subtree}" for subtree in KNOWN_SUBTREES)

PLANNER_SYSTEM_PROMPT = f"""You are a query planner for the CIR wiki assistant.

Your job is to classify the user's information need and produce a compact JSON retrieval plan.

Known site map subtrees:
{SITE_MAP}

Intent definitions:
- procedural: the user wants steps or instructions. Example: "How do I connect to SPICE?"
- inventory: the user wants a list of available equipment, software, pages, or options. Example: "What equipment is available on NatMEG?"
- definition: the user wants a direct explanation of a concept. Example: "What is OPM?"
- troubleshooting: the user describes an error, symptom, or failure. Example: "Why is my VNC screen black?"
- comparison: the user wants differences, pros/cons, or a structured comparison. Example: "What are the differences between SQUID and OPM acquisition?"
- clarify: the user is too broad or ambiguous and should choose a category first. Example: "What equipment is available on NatMEG?" when multiple equipment categories are plausible.

Rules:
- Output exactly one JSON object.
- Never invent subtree paths not present in the site map.
- Set subtree to null when unsure.
- Prefer the most specific matching subtree from the site map.
- For expanded_queries, output 2 to 4 short lexical queries, not full sentences.
- Use clarification_options only when intent is clarify.
- When intent is clarify, populate clarification_options with 3 to 6 human-readable category labels that correspond to real subtrees in the site map.
- Prefer inventory for broad list requests when a useful subtree is clear. Prefer clarify only when the user should choose between multiple real categories.

Output schema:
{{
  "intent": "procedural | inventory | definition | troubleshooting | comparison | clarify",
  "facility": "string or null",
  "subtree": "known subtree string or null",
  "expanded_queries": ["short query", "short query"],
  "top_k_override": "integer or null",
  "clarification_options": ["label", "label"]
}}
"""


@dataclass(slots=True)
class QueryPlan:
    intent: str
    facility: str | None
    subtree: str | None
    expanded_queries: list[str]
    top_k_override: int | None
    clarification_options: list[str]


def _fallback_plan(question: str) -> QueryPlan:
    return QueryPlan(
        intent="definition",
        facility=None,
        subtree=None,
        expanded_queries=[question],
        top_k_override=None,
        clarification_options=[],
    )


def _history_for_planner(question: str, history: list[ChatMessage]) -> list[ChatMessage]:
    trimmed = list(history)
    while trimmed and trimmed[-1].role == "user" and trimmed[-1].content.strip() == question.strip():
        trimmed.pop()
    return trimmed[-4:]


class QueryPlanner:
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

    def plan(self, question: str, history: list[ChatMessage]) -> QueryPlan:
        if not self._client:
            return _fallback_plan(question)

        messages = [{"role": "system", "content": PLANNER_SYSTEM_PROMPT}]
        for message in _history_for_planner(question, history):
            messages.append({"role": message.role, "content": message.content})
        messages.append(
            {
                "role": "user",
                "content": f"Question: {question}\n\nReturn only the JSON object.",
            }
        )

        try:
            response = self._client.chat.completions.create(
                model=self._settings.planning_model,
                messages=messages,
                max_completion_tokens=500,
                temperature=0.0,
                top_p=1.0,
                response_format={"type": "json_object"},
            )
            content = (response.choices[0].message.content or "").strip()
            payload = json.loads(content)
        except Exception:  # noqa: BLE001
            logger.exception("Query planner failed")
            return _fallback_plan(question)

        try:
            intent = payload["intent"] if payload["intent"] in KNOWN_INTENTS else "definition"
            facility = payload.get("facility")
            if facility is not None and not isinstance(facility, str):
                facility = None

            subtree = payload.get("subtree")
            if subtree not in KNOWN_SUBTREE_SET:
                subtree = None

            expanded_queries = [query.strip() for query in payload["expanded_queries"] if isinstance(query, str) and query.strip()]
            if not expanded_queries:
                expanded_queries = [question]

            top_k_override = payload.get("top_k_override")
            if not isinstance(top_k_override, int) or top_k_override < 1:
                top_k_override = None

            clarification_options = [
                option.strip()
                for option in payload.get("clarification_options", [])
                if isinstance(option, str) and option.strip()
            ]

            return QueryPlan(
                intent=intent,
                facility=facility,
                subtree=subtree,
                expanded_queries=expanded_queries[:4],
                top_k_override=top_k_override,
                clarification_options=clarification_options[:6],
            )
        except Exception:  # noqa: BLE001
            logger.exception("Invalid planner response payload")
            return _fallback_plan(question)
