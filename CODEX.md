# CODEX.md

This file is the entrypoint for Codex in this repository.

Do not treat this file as the full project context.
Use it as a routing guide and read only the referenced documents needed for the current task.

---

## 1. Mandatory First Step

Before making suggestions, generating code, or changing project structure:

1. Read this file.
2. Identify the current task type.
3. Read only the referenced documents needed for that task.
4. Do not load every document unless the task requires broad context.
5. Keep the implementation small unless the user explicitly asks for expansion.

---

## 2. Project Snapshot

- Project name: `rag-eval-harness`
- Purpose: CLI tool for evaluating retrieval quality of a local RAG API
- Primary role: Companion evaluation tool for `multi-agent-rag-assistant`
- Main user: Junior backend developer learning RAG internals and evaluation
- Default response language to the developer: Korean

This project answers one focused question:

```text
Did my local RAG API retrieve the expected source documents for the given questions?
```

This project is not the main RAG application.
The main RAG system is developed separately with Claude Code.

---

## 3. Document Routing Guide

### Full project handoff / background

Read:

- `HANDOFF.md`

Use this when:

- starting a new session
- recovering context after a break
- checking why this project exists
- understanding the relationship with the main RAG project

Do not read `HANDOFF.md` for every small coding task.

---

### Project context and user learning goal

Read:

- `docs/codex/project-context.md`

Use this when:

- explaining why this project exists
- connecting RAG evaluation to the user's learning goals
- deciding how much background explanation to provide

---

### MVP scope and non-goals

Read:

- `docs/codex/scope.md`

Use this when:

- deciding whether a feature belongs in v1
- avoiding scope creep
- checking explicit non-goals
- rejecting dashboard, LLM judge, database, or agent tracing requests for v1

---

### Architecture and project structure

Read:

- `docs/codex/architecture.md`

Use this when:

- creating files or folders
- deciding module responsibilities
- changing project structure
- deciding whether to import from the main RAG project

---

### CLI and API contract

Read:

- `docs/codex/cli-api-contract.md`

Use this when:

- implementing CLI commands
- calling the local RAG API
- changing endpoint behavior
- updating response normalization logic

---

### Evaluation rules and metrics

Read:

- `docs/codex/evaluation-rules.md`

Use this when:

- implementing Hit@K
- changing dataset format
- calculating pass/fail results
- generating evaluation summaries

---

### Coding rules

Read:

- `docs/codex/coding-rules.md`

Use this when:

- generating or refactoring code
- adding dependencies
- writing docstrings or comments
- deciding how much abstraction to introduce

---

### Testing and error handling

Read:

- `docs/codex/testing-error-handling.md`

Use this when:

- writing tests
- changing validation logic
- handling API failures
- improving beginner-facing error messages

---

### Future roadmap

Read:

- `docs/codex/future-roadmap.md`

Use this when:

- the user asks about later expansion
- deciding how v1 can evolve into agent tracing
- discussing `agent-trace-viewer`

Do not implement future roadmap features unless explicitly requested.

---

## 4. Working Rules

Before generating code, briefly explain:

1. Why this structure is being used
2. One simpler or alternative approach
3. Tradeoffs
4. Core concept the developer should understand

Keep the explanation short and practical.

---

## 5. Communication Rules

- Respond to the developer in Korean.
- Use English for code, function names, class names, docstrings, and configuration files.
- Use backend, Docker, AWS, CI/CD, and monitoring analogies when helpful.
- Explain RAG evaluation concepts carefully.
- Avoid long theoretical explanations that may trigger overthinking.

---

## 6. First Response Rule

When starting a new session, read this file and the necessary referenced documents.

If the user only asks you to confirm context, reply only:

```text
Context confirmed.
```

Then wait for the user's next instruction.
