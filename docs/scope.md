# Scope

This document defines the v1 MVP scope and explicit non-goals.

---

## 1. v1 Goal

Build a small Python CLI tool that evaluates whether a local RAG API retrieves expected source documents for predefined questions.

Core question:

```text
Did the RAG system retrieve the expected source document?
```

---

## 2. v1 Requirements

Implement only these in v1:

1. Load evaluation cases from a YAML file.
2. Validate that each case has:
   - `id`
   - `question`
   - `expected_sources`
   - `expected_keywords`
3. Call a local RAG API endpoint.
4. Normalize the API response into retrieved source objects.
5. Check whether expected sources appear in the top-k retrieved sources.
6. Print a Rich table.
7. Save a Markdown report.

---

## 3. Explicit Non-Goals

Do not implement these in v1:

```text
Web UI
FastAPI server
Database
Authentication
Dashboard
Background jobs
LLM-based judging
Answer quality scoring
OpenAI API integration
Claude API integration
LangGraph tracing
Agent trace viewer
Complex metric framework
```

This project evaluates retrieval quality only.
It does not evaluate final answer quality.

---

## 4. Scope Control Rule

When a requested feature seems useful but belongs beyond v1, classify it as:

```text
Deferred
```

and briefly explain why.

Example:

```text
LLM judge is useful later, but v1 should stay focused on deterministic source matching.
```

---

## 5. Good v1 Tasks

Good tasks:

```text
Add YAML dataset loader
Add dataset validation
Add Hit@K metric
Add HTTP client
Add response normalization
Add Markdown report generation
Add unit tests for pure logic
```

Bad v1 tasks:

```text
Add dashboard
Add database
Add agent trace visualization
Add LLM scoring
Add plugin system
Add scheduler
```
