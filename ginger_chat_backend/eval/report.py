from __future__ import annotations

import json
import sys
from pathlib import Path
from typing import Any

from openai import OpenAI


# Allow importing from the project root and from this eval/ directory without installation.
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
sys.path.insert(0, str(Path(__file__).resolve().parent))

from app.config import get_settings
from pairing import FEEDBACK_PATH, load_feedback, pair_feedback_with_benchmark


BENCHMARK_PATH = Path(__file__).with_name("benchmark.json")
ANSWER_PREVIEW_LENGTH = 350

REPORT_SYSTEM_PROMPT = """You are an evaluation analyst for the Ginger chat assistant.
You are given structured data about user feedback and benchmark test results.

Produce a concise Markdown evaluation report with exactly these sections:

## Feedback ratio
A short summary of the good-to-bad ratio with absolute counts.

## Good behaviours
Bullet list of specific answer qualities or topics where Ginger performed well,
based on the good feedback and any positive patterns in the paired data.

## Bad behaviours
Bullet list of specific failure patterns, retrieval misses, or wording problems
identified in the bad feedback and unmatched real-world entries.

## Actionable suggestions
Split your suggestions across exactly these three subsections. Do not add any other subsections.

### Content improvements (admin)
Numbered list of specific wiki pages to add, expand, or restructure.
Each item must name the page path or section (for example `natmeg/equipment/response-equipment/Eye-tracker/`).
No code blocks in this subsection.
If no content improvements are identified, write `None identified.`

### Code improvements
One fenced markdown code block per suggestion.
Each block must be a complete, self-contained task description a coding agent can execute without further context.
Use this exact structure inside every block:

File: <path relative to ginger_chat_backend/, with line reference if possible>
Current behaviour: <one sentence>
Desired outcome: <one sentence>
Acceptance criterion: <one concrete, testable criterion>

Relevant source locations you may reference:
- Retrieval: app/wiki_index.py
- Query planner logic: app/query_planner.py
- Answer generation: app/llm.py
If no code improvements are identified, write `None identified.`

### Prompt improvements
One fenced markdown code block per suggestion, using the same structure as Code improvements.

Relevant prompt locations you may reference:
- Chat system prompt: app/llm.py:13 (BASE_SYSTEM_PROMPT)
- Intent-specific instructions: app/llm.py:28 (INTENT_PROMPTS)
- Query planner prompt: app/query_planner.py:43 (PLANNER_SYSTEM_PROMPT)
If no prompt improvements are identified, write `None identified.`

Do not add sections other than these four. Be specific and concise."""


def _preview(text: str, limit: int = ANSWER_PREVIEW_LENGTH) -> str:
    text = " ".join(text.split())
    if len(text) <= limit:
        return text
    return f"{text[:limit].rstrip()}..."


def _format_paired(paired: list[dict[str, Any]]) -> str:
    lines = ["## Benchmark-paired feedback", ""]
    for item in paired:
        feedback_entries = item["feedback"]
        if not feedback_entries:
            continue

        benchmark = item["benchmark"]
        lines.append(f"### Benchmark: {benchmark['question']!r}")
        lines.append(f"Intent: {benchmark['intent']} | Subtree: {benchmark['expected_subtree']}")
        for feedback in feedback_entries:
            lines.append(f"- [{feedback['feedback'].upper()}] Q: {feedback['question']!r}")
            lines.append(f"  A: {_preview(feedback.get('answer', ''))}")
            if feedback.get("comment"):
                lines.append(f"  Comment: {feedback['comment']}")
        lines.append("")
    return "\n".join(lines)


def _format_unmatched(unmatched: list[dict[str, Any]]) -> str:
    if not unmatched:
        return ""

    lines = ["## Real-world feedback (no benchmark match)", ""]
    for feedback in unmatched:
        lines.append(f"- [{feedback['feedback'].upper()}] Q: {feedback['question']!r}")
        lines.append(f"  A: {_preview(feedback.get('answer', ''))}")
        if feedback.get("comment"):
            lines.append(f"  Comment: {feedback['comment']}")
        lines.append("")
    return "\n".join(lines)


def _format_ratio(feedback: list[dict[str, Any]]) -> str:
    good = sum(1 for entry in feedback if entry.get("feedback") == "good")
    bad = sum(1 for entry in feedback if entry.get("feedback") == "bad")
    total = good + bad
    ratio = f"{good}/{bad}" if bad else "N/A"
    return (
        f"Total feedback entries: {total}\n"
        f"Good: {good} | Bad: {bad} | Ratio good/bad: {ratio}\n"
    )


def generate_report() -> int:
    settings = get_settings()
    if not settings.azure_api_key:
        print("# Ginger evaluation report\n")
        print("> Cannot generate LLM report: Azure credentials not configured.")
        print("> Set GINGER_CHAT_AZURE_API_KEY and re-run.")
        return 1

    benchmark = json.loads(BENCHMARK_PATH.read_text(encoding="utf-8"))
    feedback = load_feedback(FEEDBACK_PATH)

    if not feedback:
        print("# Ginger evaluation report\n")
        print(f"> No feedback entries found in {FEEDBACK_PATH}")
        return 0

    paired, unmatched = pair_feedback_with_benchmark(benchmark, feedback)
    user_content = "\n\n".join(
        filter(
            None,
            [
                _format_ratio(feedback),
                _format_paired(paired),
                _format_unmatched(unmatched),
            ],
        )
    )

    client = OpenAI(
                api_key=settings.azure_api_key,
                base_url=settings.azure_endpoint
            )
    response = client.chat.completions.create(
        model=settings.azure_deployment,
        messages=[
            {"role": "system", "content": REPORT_SYSTEM_PROMPT},
            {"role": "user", "content": user_content},
        ],
        max_completion_tokens=3000,
        temperature=0.3,
    )

    report = (response.choices[0].message.content or "").strip()
    if not report:
        print("# Ginger evaluation report\n")
        print("> LLM returned an empty report.")
        return 1

    print("# Ginger evaluation report\n")
    print(report)
    return 0


if __name__ == "__main__":
    raise SystemExit(generate_report())
