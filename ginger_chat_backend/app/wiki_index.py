from __future__ import annotations

import math
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable
from urllib.parse import quote, urlparse


FRONT_MATTER_PATTERN = re.compile(r"\A---\s*\n(.*?)\n---\s*\n", re.DOTALL)
TITLE_PATTERN = re.compile(r"^title:\s*(.+?)\s*$", re.MULTILINE)
HEADING_PATTERN = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TOKEN_PATTERN = re.compile(r"[0-9A-Za-zÅÄÖåäö][0-9A-Za-zÅÄÖåäö_\-]{1,}")

PATH_TOKEN_BOOST = 3.0
SUBTREE_FALLBACK_SCORE_RATIO = 2.0
SUBTREE_FALLBACK_SCORE_MARGIN = 10.0

STOPWORDS = {
    "about",
    "all",
    "also",
    "an",
    "and",
    "are",
    "att",
    "av",
    "can",
    "could",
    "den",
    "det",
    "did",
    "do",
    "does",
    "eller",
    "en",
    "ett",
    "for",
    "fran",
    "from",
    "får",
    "för",
    "ha",
    "har",
    "has",
    "have",
    "how",
    "hur",
    "i",
    "if",
    "in",
    "inte",
    "is",
    "kan",
    "med",
    "men",
    "not",
    "och",
    "of",
    "om",
    "on",
    "or",
    "som",
    "should",
    "ska",
    "skulle",
    "så",
    "that",
    "the",
    "this",
    "there",
    "to",
    "vad",
    "var",
    "vart",
    "when",
    "where",
    "which",
    "who",
    "why",
    "will",
    "with",
    "would",
}


def _normalise_whitespace(value: str) -> str:
    return re.sub(r"\s+", " ", value).strip()


def _extract_front_matter(text: str) -> str | None:
    match = FRONT_MATTER_PATTERN.match(text)
    return match.group(1) if match else None


def _strip_front_matter(text: str) -> str:
    return FRONT_MATTER_PATTERN.sub("", text, count=1)


def _extract_title(text: str, fallback: str) -> str:
    front_matter = _extract_front_matter(text)
    if front_matter:
        title_match = TITLE_PATTERN.search(front_matter)
        if title_match:
            return title_match.group(1).strip().strip('"')

    for line in _strip_front_matter(text).splitlines():
        if line.startswith("# "):
            return line[2:].strip()

    return fallback.replace("-", " ").replace("_", " ").strip()


def _tokenize(value: str) -> list[str]:
    normalized = value.replace("-", " ")
    return [token.lower() for token in TOKEN_PATTERN.findall(normalized)]


def _filter_index_tokens(tokens: Iterable[str]) -> list[str]:
    return [token for token in tokens if token not in STOPWORDS]


def _path_tokens(path: Path, docs_root: Path) -> set[str]:
    relative_path = path.relative_to(docs_root)
    path_parts = list(relative_path.parts[:-1])
    if relative_path.name != "index.md":
        path_parts.append(relative_path.stem)

    tokens: set[str] = set()
    for part in path_parts:
        tokens.update(_filter_index_tokens(_tokenize(part)))
    return tokens


def _normalise_subtree_prefix(prefix: str | None) -> str | None:
    if not prefix:
        return None

    cleaned = prefix.strip().strip("/")
    if not cleaned:
        return None
    return f"/{cleaned}/"


def _url_matches_subtree(url: str, prefix: str) -> bool:
    parsed = urlparse(url)
    path = parsed.path or url
    if not path.endswith("/"):
        path = f"{path}/"
    return path.startswith(prefix)


def _path_to_url(path: Path, docs_root: Path, site_base_url: str) -> str:
    relative_path = path.relative_to(docs_root)
    parts = list(relative_path.parts)

    if relative_path.name == "index.md":
        url_parts = parts[:-1]
    else:
        url_parts = [*parts[:-1], relative_path.stem]

    relative_url = "/" + "/".join(quote(part) for part in url_parts if part)
    if not relative_url.endswith("/"):
        relative_url += "/"

    if not url_parts:
        relative_url = "/"

    return f"{site_base_url}{relative_url}" if site_base_url else relative_url


def _iter_section_chunks(text: str, title: str, chunk_size: int, chunk_overlap: int) -> Iterable[tuple[str | None, str]]:
    lines = _strip_front_matter(text).splitlines()
    heading_stack: list[str] = []
    section_heading: str | None = None
    buffer: list[str] = []

    def flush_buffer() -> Iterable[tuple[str | None, str]]:
        content = _normalise_whitespace("\n".join(buffer))
        if not content:
            return []
        return _split_large_chunk(content, section_heading or title, chunk_size, chunk_overlap)

    for line in lines:
        heading_match = HEADING_PATTERN.match(line)
        if heading_match:
            for chunk in flush_buffer():
                yield chunk

            level = len(heading_match.group(1))
            heading_text = heading_match.group(2).strip()
            heading_stack[:] = heading_stack[: level - 1]
            heading_stack.append(heading_text)
            section_heading = " > ".join(heading_stack)
            buffer = [line]
            continue

        buffer.append(line)

    for chunk in flush_buffer():
        yield chunk


def _split_large_chunk(content: str, heading: str, chunk_size: int, chunk_overlap: int) -> Iterable[tuple[str, str]]:
    if len(content) <= chunk_size:
        return [(heading, content)]

    chunks: list[tuple[str, str]] = []
    start = 0
    while start < len(content):
        end = min(len(content), start + chunk_size)
        if end < len(content):
            split_at = content.rfind(" ", start, end)
            if split_at > start + 200:
                end = split_at

        piece = content[start:end].strip()
        if piece:
            chunks.append((heading, piece))

        if end >= len(content):
            break

        start = max(end - chunk_overlap, start + 1)

    return chunks


@dataclass(slots=True)
class IndexedChunk:
    title: str
    url: str
    section: str | None
    content: str
    snippet: str
    token_counts: Counter[str]
    token_set: set[str]
    path_token_set: set[str]


@dataclass(slots=True)
class SearchResult:
    score: float
    chunk: IndexedChunk


class WikiIndex:
    def __init__(self, docs_root: Path, chunks: list[IndexedChunk], *, idf: dict[str, float] | None = None) -> None:
        self.docs_root = docs_root
        self.chunks = chunks
        self._idf = idf if idf is not None else self._build_idf(chunks)

    @classmethod
    def build(cls, docs_root: Path, site_base_url: str, chunk_size: int, chunk_overlap: int) -> "WikiIndex":
        chunks: list[IndexedChunk] = []

        for path in sorted(docs_root.rglob("*.md")):
            raw_text = path.read_text(encoding="utf-8")
            title = _extract_title(raw_text, path.stem)
            url = _path_to_url(path, docs_root, site_base_url)
            path_token_set = _path_tokens(path, docs_root)

            for section, content in _iter_section_chunks(raw_text, title, chunk_size, chunk_overlap):
                tokens = _filter_index_tokens(_tokenize(f"{title} {section or ''} {content}"))
                if not tokens and not path_token_set:
                    continue

                snippet = _normalise_whitespace(content)[:280]
                chunks.append(
                    IndexedChunk(
                        title=title,
                        url=url,
                        section=section,
                        content=content,
                        snippet=snippet,
                        token_counts=Counter(tokens),
                        token_set=set(tokens),
                        path_token_set=path_token_set,
                    )
                )

        return cls(docs_root=docs_root, chunks=chunks)

    @staticmethod
    def _build_idf(chunks: list[IndexedChunk]) -> dict[str, float]:
        total_chunks = max(1, len(chunks))
        document_frequency: Counter[str] = Counter()
        for chunk in chunks:
            document_frequency.update(chunk.token_set)
            document_frequency.update(chunk.path_token_set)
        return {
            token: math.log((1 + total_chunks) / (1 + frequency)) + 1.0
            for token, frequency in document_frequency.items()
        }

    def search(self, query: str, limit: int) -> list[SearchResult]:
        query_tokens = _filter_index_tokens(_tokenize(query))
        if not query_tokens:
            return []

        unique_tokens = set(query_tokens)
        results: list[SearchResult] = []
        for chunk in self.chunks:
            overlap = unique_tokens & chunk.token_set
            path_overlap = unique_tokens & chunk.path_token_set
            if not overlap and not path_overlap:
                continue

            score = 0.0
            for token in overlap:
                score += self._idf.get(token, 1.0) * (1.0 + math.log(chunk.token_counts[token]))

            for token in path_overlap:
                score += self._idf.get(token, 1.0) * PATH_TOKEN_BOOST

            title_tokens = set(_filter_index_tokens(_tokenize(chunk.title)))
            section_tokens = set(_filter_index_tokens(_tokenize(chunk.section or "")))
            score += len(unique_tokens & title_tokens) * 2.0
            score += len(unique_tokens & section_tokens) * 1.0

            results.append(SearchResult(score=score, chunk=chunk))

        results.sort(key=lambda result: result.score, reverse=True)
        return results[:limit]

    def subtree_filter(self, prefix: str | None) -> "WikiIndex":
        normalised_prefix = _normalise_subtree_prefix(prefix)
        if not normalised_prefix:
            return self

        filtered_chunks = [chunk for chunk in self.chunks if _url_matches_subtree(chunk.url, normalised_prefix)]
        return WikiIndex(self.docs_root, filtered_chunks, idf=self._idf)

    def search_multi(self, queries: list[str], limit: int, subtree: str | None = None) -> list[SearchResult]:
        def run(index: WikiIndex) -> list[SearchResult]:
            merged: dict[tuple[str, str | None], SearchResult] = {}
            for query in queries:
                for result in index.search(query, limit=limit):
                    key = (result.chunk.url, result.chunk.section)
                    previous = merged.get(key)
                    if previous is None or result.score > previous.score:
                        merged[key] = result

            ranked = sorted(merged.values(), key=lambda result: result.score, reverse=True)
            return ranked[:limit]

        scoped_index = self.subtree_filter(subtree)
        results = run(scoped_index)
        if subtree:
            global_results = run(self)
            if not results:
                return global_results
            if global_results and global_results[0].score >= max(
                results[0].score * SUBTREE_FALLBACK_SCORE_RATIO,
                results[0].score + SUBTREE_FALLBACK_SCORE_MARGIN,
            ):
                return global_results
        return results

    def aggregate_by_page(self, results: list[SearchResult], page_limit: int) -> list[SearchResult]:
        page_scores: dict[str, float] = defaultdict(float)
        representatives: dict[str, SearchResult] = {}

        for result in results:
            url = result.chunk.url
            page_scores[url] += result.score
            current = representatives.get(url)
            if current is None or result.score > current.score:
                representatives[url] = result

        aggregated = [
            SearchResult(score=page_scores[url], chunk=representatives[url].chunk)
            for url in representatives
        ]
        aggregated.sort(key=lambda result: result.score, reverse=True)
        return aggregated[:page_limit]
