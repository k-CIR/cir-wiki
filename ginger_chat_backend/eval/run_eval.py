from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from typing import Any
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen


DEFAULT_BASE_URL = os.getenv("GINGER_CHAT_EVAL_BASE_URL") or os.getenv("ZIGGA_CHAT_EVAL_BASE_URL", "http://127.0.0.1:8001")
BENCHMARK_PATH = Path(__file__).with_name("benchmark.json")


def _get_json(url: str) -> dict[str, Any]:
    request = Request(url, method="GET")
    with urlopen(request, timeout=5) as response:  # noqa: S310
        return json.loads(response.read().decode("utf-8"))


def _post_json(url: str, payload: dict[str, Any]) -> dict[str, Any]:
    request = Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={"Content-Type": "application/json"},
        method="POST",
    )
    with urlopen(request, timeout=20) as response:  # noqa: S310
        return json.loads(response.read().decode("utf-8"))


def _load_benchmark() -> list[dict[str, Any]]:
    return json.loads(BENCHMARK_PATH.read_text(encoding="utf-8"))


def main() -> int:
    base_url = DEFAULT_BASE_URL.rstrip("/")

    try:
        health = _get_json(f"{base_url}/health")
    except (HTTPError, URLError, TimeoutError, json.JSONDecodeError) as exc:
        print(f"Backend is unreachable at {base_url}. Start the backend before running eval. Error: {exc}")
        return 1

    print(f"Health OK: indexed_chunks={health.get('indexed_chunks')} azure_configured={health.get('azure_configured')}")

    benchmark = _load_benchmark()
    retrieval_hits = 0
    grounded_hits = 0
    clarification_hits = 0

    for index, entry in enumerate(benchmark, start=1):
        response = _post_json(
            f"{base_url}/api/chat",
            {
                "message": entry["question"],
                "history": [],
                "page_context": None,
            },
        )

        source_urls = [source.get("url", "") for source in response.get("sources", [])]
        matched_urls = [
            expected
            for expected in entry["expected_source_urls"]
            if any(expected in actual for actual in source_urls)
        ]
        hit = bool(matched_urls)
        if hit:
            retrieval_hits += 1
        if response.get("grounded"):
            grounded_hits += 1

        plan = response.get("plan") or {}
        actual_intent = plan.get("intent")
        if actual_intent == "clarify":
            clarification_hits += 1

        print(f"[{index:02d}] {entry['question']}")
        print(f"  expected intent: {entry['intent']}")
        print(f"  planner intent:  {actual_intent}")
        print(f"  expected subtree:{entry['expected_subtree']}")
        print(f"  planner subtree: {plan.get('subtree')}")
        print(f"  grounded:        {response.get('grounded')}")
        print(f"  retrieval hit:   {'yes' if hit else 'no'}")
        print(f"  matched urls:    {matched_urls or ['-']}")
        print(f"  sources:         {source_urls or ['-']}")

    total = max(1, len(benchmark))
    hit_rate = retrieval_hits / total
    grounded_rate = grounded_hits / total
    clarification_rate = clarification_hits / total

    print("\nSummary")
    print(f"  retrieval hit rate: {retrieval_hits}/{total} ({hit_rate:.0%})")
    print(f"  groundedness rate:  {grounded_hits}/{total} ({grounded_rate:.0%})")
    print(f"  clarification rate: {clarification_hits}/{total} ({clarification_rate:.0%})")

    return 0 if hit_rate >= 0.70 else 1


if __name__ == "__main__":
    sys.exit(main())
