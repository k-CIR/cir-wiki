from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any


FEEDBACK_PATH = Path(__file__).with_name("feedback.jsonl")
BENCHMARK_PATH = Path(__file__).with_name("benchmark.json")

_STOPWORDS = {
    "a",
    "an",
    "the",
    "is",
    "are",
    "was",
    "were",
    "be",
    "been",
    "do",
    "does",
    "did",
    "at",
    "in",
    "on",
    "to",
    "for",
    "of",
    "and",
    "or",
    "not",
    "there",
    "how",
    "what",
    "where",
    "why",
    "which",
    "who",
    "with",
    "can",
    "could",
    "would",
    "should",
    "i",
    "you",
    "we",
    "my",
    "your",
}


def _tokens(text: str) -> set[str]:
    words = re.findall(r"[a-z0-9]+", text.lower())
    return {word for word in words if word not in _STOPWORDS}


def _jaccard(a: set[str], b: set[str]) -> float:
    if not a and not b:
        return 1.0
    union = a | b
    return len(a & b) / len(union)


def load_feedback(path: Path = FEEDBACK_PATH) -> list[dict[str, Any]]:
    """Load all feedback entries from a JSONL file."""

    if not path.exists():
        return []

    entries: list[dict[str, Any]] = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            entries.append(json.loads(line))
    return entries


def pair_feedback_with_benchmark(
    benchmark: list[dict[str, Any]],
    feedback: list[dict[str, Any]],
    threshold: float = 0.5,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Pair feedback entries with benchmark entries by question similarity."""

    bench_tokens = [(entry, _tokens(entry["question"])) for entry in benchmark]
    paired: list[dict[str, Any]] = [{"benchmark": entry, "feedback": []} for entry in benchmark]
    unmatched: list[dict[str, Any]] = []

    for fb in feedback:
        fb_tokens = _tokens(fb.get("question", ""))
        best_score = 0.0
        best_index = -1

        for index, (_, benchmark_tokens) in enumerate(bench_tokens):
            score = _jaccard(fb_tokens, benchmark_tokens)
            if score > best_score:
                best_score = score
                best_index = index

        if best_score >= threshold:
            paired[best_index]["feedback"].append(fb)
        else:
            unmatched.append(fb)

    return paired, unmatched


def main() -> int:
    benchmark = json.loads(BENCHMARK_PATH.read_text(encoding="utf-8"))
    feedback = load_feedback(FEEDBACK_PATH)
    paired, unmatched = pair_feedback_with_benchmark(benchmark, feedback)
    matched_feedback = sum(len(item["feedback"]) for item in paired)
    paired_benchmarks = sum(1 for item in paired if item["feedback"])

    print(f"Benchmark entries: {len(benchmark)}")
    print(f"Feedback entries: {len(feedback)}")
    print(f"Benchmarks with matches: {paired_benchmarks}")
    print(f"Matched feedback entries: {matched_feedback}")
    print(f"Unmatched feedback entries: {len(unmatched)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
