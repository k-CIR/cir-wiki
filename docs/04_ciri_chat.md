# CIRI (CIR Information Retrieval Interface)

CIRI is the CIR wiki chat assistant. It answers questions using content from this wiki and is intended to help users find the right page, section, or workflow more quickly.

## What CIRI does

- answers questions about CIR wiki content
- grounds answers in indexed documentation when possible
- turns citations into inline links in the answer text
- asks the user to choose a category when a question is too broad
- shows a contribution nudge when no confident grounded answer was found
- collects thumbs-up / thumbs-down feedback for development

## Where the chat appears

The chat UI is injected into the MkDocs site by:

- `docs/javascripts/ginger-chat.js`
- `docs/assets/ginger-chat.css`
- `mkdocs.yml`

The widget is currently configured to enable itself automatically on local development hosts (`localhost` and `127.0.0.1`). Its default backend URL is `http://127.0.0.1:8000`.

## User-facing behaviour

### Grounded answers

When CIRI finds relevant wiki content, it returns an answer based on the indexed documentation. Citation markers are converted into inline Markdown links that open the relevant wiki page in a new tab.

### Clarification answers

If a question is too broad, CIRI may ask the user to choose between several categories first. These options are rendered as clickable links to the corresponding wiki sections.

### No grounded answer

If CIRI cannot find a confident grounded answer, it marks the response as ungrounded and shows a short prompt linking to the page for contributing to the wiki:

- `/03_contribute_to_wiki/`

### Feedback and logging notice

Each assistant response can show:

- 👍 for a useful answer
- 👎 for an unhelpful answer, with an optional free-text comment

The chat footer also displays a permanent notice that conversations are logged for development purposes.

## Privacy and logging

The current implementation logs development feedback to:

- `ginger_chat_backend/eval/feedback.jsonl`

Each feedback entry contains:

- timestamp
- message ID
- preceding user question
- assistant answer
- feedback type (`good` or `bad`)
- optional comment

Contributors should treat this file as development data and review its handling carefully before enabling CIRI in broader environments.

## Architecture overview

### Frontend

The browser-side chat code is in:

- `docs/javascripts/ginger-chat.js`
- `docs/assets/ginger-chat.css`

Responsibilities include:

- rendering the chat panel
- sending messages to the backend
- rendering Markdown answers using `marked`
- applying external-link attributes
- showing feedback controls and the contribution nudge
- posting feedback to the backend

### Backend

The backend is a FastAPI app in `ginger_chat_backend/app/`.

Important files:

- `main.py` — API routes, citation/link formatting, feedback logging
- `models.py` — request and response models
- `llm.py` — answer generation and citation extraction
- `query_planner.py` — retrieval planning and clarification categories
- `wiki_index.py` — indexing and retrieval over the docs tree

Main endpoints:

- `GET /health`
- `POST /api/chat`
- `POST /api/feedback`

## Running CIRI locally

### 1. Install backend dependencies

```bash
cd ginger_chat_backend
pip install -r requirements.txt
```

### 2. Start the backend

```bash
uvicorn app.main:app --reload
```

By default the local frontend expects the backend at `http://127.0.0.1:8000`.

### 3. Start the wiki site

From the repository root:

```bash
mkdocs serve
```

Open the local MkDocs URL in a browser. On local hosts, the CIRI button should be visible.

## Configuration

The backend reads its settings from environment variables in `ginger_chat_backend/app/config.py`.

Current variables include:

- `GINGER_CHAT_DOCS_ROOT`
- `GINGER_CHAT_AZURE_API_KEY`
- `CIR_AZURE_API`
- `GINGER_CHAT_AZURE_ENDPOINT`
- `GINGER_CHAT_AZURE_API_VERSION`
- `GINGER_CHAT_AZURE_DEPLOYMENT`
- `GINGER_CHAT_PLANNING_MODEL`
- `GINGER_CHAT_ALLOWED_ORIGINS`
- `GINGER_CHAT_RETRIEVAL_TOP_K`
- `GINGER_CHAT_CHUNK_SIZE`
- `GINGER_CHAT_CHUNK_OVERLAP`
- `GINGER_CHAT_SOURCE_CHAR_LIMIT`
- `GINGER_CHAT_SITE_BASE_URL`
- `GINGER_CHAT_EVAL_BASE_URL`

Notes:
- `GINGER_CHAT_DOCS_ROOT` controls which docs tree is indexed
- `GINGER_CHAT_SITE_BASE_URL` is used when building source URLs

## Frontend runtime configuration

The frontend can be adjusted through `window.__GINGER_CHAT_CONFIG__` before `ginger-chat.js` runs.

Supported runtime keys in the current implementation are:

- `assistantName`
- `apiBaseUrl`
- `enabled`
- `maxHistoryMessages`
- `placeholder`
- `welcomeMessage`

## Content and answer formatting

CIRI formats answers in a few specific ways:

- Markdown in answers is rendered with `marked`
- citation markers such as `[N]` are normalized into inline Markdown links in the backend
- assistant sources are still returned in the API payload, even though the separate sources card is no longer rendered in the UI
- clarification options are formatted as linked bullet items when the option can be mapped to a known wiki route

## Development notes

- The chat widget is currently optimized for local development and evaluation.
- The frontend rebuilds the message list on every render, so message-level UI state is stored directly on `state.messages` objects.
- Feedback submission is fire-and-forget on the frontend; failed feedback requests do not interrupt chat usage.
- `open(..., "a")` creates `feedback.jsonl` automatically if it does not already exist.

## Validation checklist

When changing CIRI, verify at least the following:

1. local MkDocs pages load the chat widget
2. `POST /api/chat` returns answers and renders Markdown correctly
3. inline citation links open the expected pages
4. clarification options render as links when available
5. ungrounded answers show the contribution nudge
6. 👍 and 👎 feedback create entries in `ginger_chat_backend/feedback.jsonl`
7. the logging notice remains visible in the chat footer
8. backend syntax checks and frontend syntax checks still pass
