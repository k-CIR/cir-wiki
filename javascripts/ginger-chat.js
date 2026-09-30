(() => {
  if (typeof marked !== "undefined" && !window.__gingerChatMarkedConfigured) {
    marked.use({ breaks: true, gfm: true });
    window.__gingerChatMarkedConfigured = true;
  }

  const localHosts = new Set(["127.0.0.1", "localhost"]);
  const isLocal = localHosts.has(window.location.hostname);
  const runtimeConfig = {
    assistantName: "CIRI",
    apiBaseUrl: isLocal ? "http://127.0.0.1:8000" : "",
    enabled: isLocal,
    maxHistoryMessages: 6,
    placeholder: "Ask a question about the CIR wiki…",
    welcomeMessage:
      "Ask about CIR wiki content. Answers are grounded in the documentation and include source links when available.",
    ...(window.__GINGER_CHAT_CONFIG__ || {}),
  };

  const state = window.__gingerChatState || {
    isOpen: false,
    isSending: false,
    messages: [
      {
        role: "assistant",
        content: runtimeConfig.welcomeMessage,
        sources: [],
      },
    ],
    status: "",
    error: "",
  };
  window.__gingerChatState = state;

  function escapeHtml(value) {
    return value
      .replaceAll("&", "&amp;")
      .replaceAll("<", "&lt;")
      .replaceAll(">", "&gt;")
      .replaceAll('"', "&quot;")
      .replaceAll("'", "&#39;");
  }

  function renderMarkdown(text) {
    if (typeof marked === "undefined") {
      return escapeHtml(text).replaceAll("\n", "<br>");
    }

    return marked.parse(text);
  }

  function setExternalLinkAttrs(container) {
    container.querySelectorAll("a").forEach((link) => {
      link.target = "_blank";
      link.rel = "noopener noreferrer";
    });
  }

  function buildTypingEl() {
    const message = document.createElement("div");
    message.className = "ginger-chat__message ginger-chat__message--assistant";

    const dots = document.createElement("div");
    dots.className = "ginger-chat__typing";
    for (let index = 0; index < 3; index += 1) {
      dots.appendChild(document.createElement("span"));
    }

    message.appendChild(dots);
    return message;
  }

  function autoResizeTextarea(textarea) {
    textarea.style.height = "auto";
    textarea.style.height = `${textarea.scrollHeight}px`;
  }

  function currentPageContext() {
    const title = document.querySelector("h1")?.textContent?.trim() || document.title;
    return {
      title,
      url: `${window.location.pathname}${window.location.search}`,
    };
  }

  function toHistoryPayload() {
    return state.messages
      .filter((message) => message.role === "assistant" || message.role === "user")
      .slice(-runtimeConfig.maxHistoryMessages)
      .map(({ role, content }) => ({ role, content }));
  }

  function setOpen(nextValue) {
    state.isOpen = nextValue;
    render();
  }

  function setSending(nextValue, status) {
    state.isSending = nextValue;
    if (typeof status === "string") {
      state.status = status;
    }
    if (nextValue) {
      state.error = "";
    }
    render();
  }

  async function sendMessage(text) {
    const trimmed = text.trim();
    if (!trimmed || state.isSending) {
      return;
    }

    if (!runtimeConfig.apiBaseUrl) {
      state.error = "CIRI is not configured with a backend API URL.";
      render();
      return;
    }

    state.messages.push({ role: "user", content: trimmed, sources: [] });
    setSending(true, "Searching the wiki and generating an answer…");

    try {
      const response = await fetch(`${runtimeConfig.apiBaseUrl.replace(/\/$/, "")}/api/chat`, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({
          message: trimmed,
          history: toHistoryPayload(),
          page_context: currentPageContext(),
        }),
      });

      if (!response.ok) {
        const body = await response.text();
        throw new Error(body || `Request failed with status ${response.status}`);
      }

      const payload = await response.json();
      state.messages.push({
        role: "assistant",
        content: payload.answer || "No answer was returned.",
        sources: Array.isArray(payload.sources) ? payload.sources : [],
        messageId: payload.message_id || "",
        grounded: payload.grounded !== false,
        feedback: null,
        feedbackSubmitted: false,
      });
      state.status = payload.grounded
        ? "Answer generated from CIR wiki content."
        : "No confident grounded answer was found in the wiki.";
    } catch (error) {
      state.error = error instanceof Error ? error.message : "Unexpected CIRI chat error.";
    } finally {
      setSending(false);
    }
  }

  function findQuestion(msgIndex) {
    for (let index = msgIndex - 1; index >= 0; index -= 1) {
      if (state.messages[index].role === "user") {
        return state.messages[index].content;
      }
    }
    return "";
  }

  async function postFeedback(messageId, answer, feedback, comment) {
    if (!runtimeConfig.apiBaseUrl) {
      return;
    }

    const question = findQuestion(state.messages.findIndex((message) => message.messageId === messageId));
    try {
      await fetch(`${runtimeConfig.apiBaseUrl.replace(/\/$/, "")}/api/feedback`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          message_id: messageId,
          question,
          answer,
          feedback,
          comment,
        }),
      });
    } catch {
      // Fire-and-forget feedback should not affect chat UX.
    }
  }

  function renderMessages(container) {
    container.innerHTML = "";

    for (const message of state.messages) {
      const messageEl = document.createElement("div");
      messageEl.className = `ginger-chat__message ginger-chat__message--${message.role}`;

      const contentEl = document.createElement("div");
      contentEl.className = "ginger-chat__content";
      if (message.role === "assistant") {
        contentEl.innerHTML = renderMarkdown(message.content);
        setExternalLinkAttrs(contentEl);
      } else {
        contentEl.textContent = message.content;
      }
      messageEl.appendChild(contentEl);

      if (message.role === "assistant" && message.grounded === false) {
        const nudge = document.createElement("p");
        nudge.className = "ginger-chat__contribute-nudge";
        nudge.innerHTML =
          'Can\'t find what you\'re looking for? <a href="/03_contribute_to_wiki/" target="_blank" rel="noopener noreferrer">Contribute to the wiki ↗</a>';
        messageEl.appendChild(nudge);
      }

      if (message.role === "assistant" && message.messageId) {
        const bar = document.createElement("div");
        bar.className = "ginger-chat__feedback-bar";

        const goodBtn = document.createElement("button");
        goodBtn.type = "button";
        goodBtn.className = `ginger-chat__feedback-btn${message.feedback === "good" ? " ginger-chat__feedback-btn--active" : ""}`;
        goodBtn.setAttribute("aria-label", "Good response");
        goodBtn.textContent = "👍";

        const badBtn = document.createElement("button");
        badBtn.type = "button";
        badBtn.className = `ginger-chat__feedback-btn${message.feedback === "bad" ? " ginger-chat__feedback-btn--active" : ""}`;
        badBtn.setAttribute("aria-label", "Bad response");
        badBtn.textContent = "👎";

        bar.appendChild(goodBtn);
        bar.appendChild(badBtn);
        messageEl.appendChild(bar);

        const form = document.createElement("div");
        form.className = "ginger-chat__feedback-form";
        form.hidden = message.feedback !== "bad" || message.feedbackSubmitted;

        const label = document.createElement("label");
        label.className = "ginger-chat__feedback-label";
        label.textContent = "What was wrong or missing?";

        const textarea = document.createElement("textarea");
        textarea.className = "ginger-chat__feedback-textarea";
        textarea.placeholder = "Optional - describe what you expected...";
        textarea.rows = 3;

        const actions = document.createElement("div");
        actions.className = "ginger-chat__feedback-actions";

        const submitBtn = document.createElement("button");
        submitBtn.type = "button";
        submitBtn.className = "ginger-chat__feedback-submit";
        submitBtn.textContent = "Send";

        const cancelBtn = document.createElement("button");
        cancelBtn.type = "button";
        cancelBtn.className = "ginger-chat__feedback-cancel";
        cancelBtn.textContent = "Cancel";

        actions.appendChild(submitBtn);
        actions.appendChild(cancelBtn);
        form.appendChild(label);
        form.appendChild(textarea);
        form.appendChild(actions);
        messageEl.appendChild(form);

        const msgIndex = state.messages.indexOf(message);

        goodBtn.addEventListener("click", () => {
          if (state.messages[msgIndex].feedbackSubmitted || state.messages[msgIndex].feedback === "good") {
            return;
          }
          state.messages[msgIndex].feedback = "good";
          state.messages[msgIndex].feedbackSubmitted = true;
          postFeedback(message.messageId, message.content, "good", "");
          render();
        });

        badBtn.addEventListener("click", () => {
          if (state.messages[msgIndex].feedbackSubmitted) {
            return;
          }
          state.messages[msgIndex].feedback = "bad";
          render();
        });

        cancelBtn.addEventListener("click", () => {
          state.messages[msgIndex].feedback = null;
          render();
        });

        submitBtn.addEventListener("click", () => {
          if (state.messages[msgIndex].feedbackSubmitted) {
            return;
          }
          const comment = textarea.value.trim();
          state.messages[msgIndex].feedback = "bad";
          state.messages[msgIndex].feedbackSubmitted = true;
          postFeedback(message.messageId, message.content, "bad", comment);
          render();
        });
      }

      container.appendChild(messageEl);
    }

    if (state.isSending) {
      container.appendChild(buildTypingEl());
    }

    container.scrollTop = container.scrollHeight;
  }

  function render() {
    const root = document.getElementById("ginger-chat-root");
    if (!root) {
      return;
    }

    const panel = root.querySelector(".ginger-chat__panel");
    const toggle = root.querySelector(".ginger-chat__toggle");
    const textarea = root.querySelector(".ginger-chat__input");
    const submit = root.querySelector(".ginger-chat__submit");
    const statusMsg = root.querySelector(".ginger-chat__status-msg");
    const messages = root.querySelector(".ginger-chat__messages");

    panel.hidden = !state.isOpen;
    toggle.setAttribute("aria-expanded", String(state.isOpen));
    submit.disabled = state.isSending;
    textarea.disabled = state.isSending;
    statusMsg.textContent = state.error || state.status;
    statusMsg.className = state.error ? "ginger-chat__status-msg ginger-chat__status-msg--error" : "ginger-chat__status-msg";
    renderMessages(messages);
    autoResizeTextarea(textarea);
  }

  function mount() {
    if (!runtimeConfig.enabled || document.getElementById("ginger-chat-root")) {
      return;
    }

    const root = document.createElement("div");
    root.id = "ginger-chat-root";
    root.className = "ginger-chat";
    root.innerHTML = `
      <section class="ginger-chat__panel" hidden aria-label="${escapeHtml(runtimeConfig.assistantName)} conversation">
        <header class="ginger-chat__header">
          <div>
            <h2 class="ginger-chat__title">${escapeHtml(runtimeConfig.assistantName)}</h2>
            <p class="ginger-chat__subtitle">Grounded answers from the CIR wiki</p>
          </div>
          <button class="ginger-chat__close" type="button" aria-label="Close chat">×</button>
        </header>
        <div class="ginger-chat__messages" aria-live="polite"></div>
        <form class="ginger-chat__composer">
          <textarea class="ginger-chat__input" name="message" placeholder="${escapeHtml(runtimeConfig.placeholder)}"></textarea>
          <button class="ginger-chat__submit" type="submit">Send</button>
        </form>
        <div class="ginger-chat__status">
          <span class="ginger-chat__status-msg"></span>
          <span class="ginger-chat__log-notice">Conversations are logged for development purposes.</span>
        </div>
      </section>
      <button class="ginger-chat__toggle" type="button" aria-controls="ginger-chat-root" aria-expanded="false">
        Ask ${escapeHtml(runtimeConfig.assistantName)}
      </button>`;

    root.querySelector(".ginger-chat__toggle")?.addEventListener("click", () => setOpen(!state.isOpen));
    root.querySelector(".ginger-chat__close")?.addEventListener("click", () => setOpen(false));
    root.querySelector(".ginger-chat__composer")?.addEventListener("submit", async (event) => {
      event.preventDefault();
      const textarea = root.querySelector(".ginger-chat__input");
      const text = textarea.value;
      textarea.value = "";
      autoResizeTextarea(textarea);
      await sendMessage(text);
    });

    root.querySelector(".ginger-chat__input")?.addEventListener("keydown", (event) => {
      if (event.key === "Enter" && !event.shiftKey) {
        event.preventDefault();
        root.querySelector(".ginger-chat__composer")?.dispatchEvent(new Event("submit", { cancelable: true }));
      }
    });

    root.querySelector(".ginger-chat__input")?.addEventListener("input", (event) => {
      autoResizeTextarea(event.currentTarget);
    });

    document.body.appendChild(root);
    render();
  }

  if (typeof document$ !== "undefined" && document$.subscribe) {
    document$.subscribe(() => mount());
  } else {
    window.addEventListener("DOMContentLoaded", mount, { once: true });
  }
})();
