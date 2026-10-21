from __future__ import annotations

import uuid
from typing import Literal

from pydantic import BaseModel, Field


class PageContext(BaseModel):
    title: str | None = None
    url: str | None = None


class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str = Field(min_length=1, max_length=4000)


class ChatRequest(BaseModel):
    message: str = Field(min_length=1, max_length=4000)
    history: list[ChatMessage] = Field(default_factory=list)
    page_context: PageContext | None = None


class SourceItem(BaseModel):
    title: str
    url: str
    section: str | None = None
    snippet: str | None = None


class QueryPlan(BaseModel):
    intent: str
    facility: str | None = None
    subtree: str | None = None
    expanded_queries: list[str] = Field(default_factory=list)
    top_k_override: int | None = None
    clarification_options: list[str] = Field(default_factory=list)


class ChatResponse(BaseModel):
    answer: str
    sources: list[SourceItem] = Field(default_factory=list)
    grounded: bool = True
    plan: QueryPlan | None = None
    message_id: str = Field(default_factory=lambda: str(uuid.uuid4()))


class FeedbackRequest(BaseModel):
    message_id: str
    question: str
    answer: str
    feedback: Literal["good", "bad"]
    comment: str | None = None


class HealthResponse(BaseModel):
    status: str
    docs_root: str
    indexed_chunks: int
    azure_configured: bool
