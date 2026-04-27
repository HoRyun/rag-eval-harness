# RAG Eval Harness - Handoff Document

This document provides broad context for continuing the `rag-eval-harness` project in a new AI coding session.

Do not read this file for every small task.
Use it when starting fresh, recovering context, or checking why this project exists.

---

## 1. Project Identity

- Project name: `rag-eval-harness`
- Project type: Local Python CLI tool
- Primary AI tool: Codex
- Main language: Python 3.12
- Package manager: uv
- Goal: Evaluate whether a local RAG API retrieves the expected source documents for a set of predefined test questions.

This project is a companion tool for the main project:

```text
multi-agent-rag-assistant
```

The main project is developed with Claude Code.
This project is developed with Codex.

---

## 2. Why This Project Exists

The developer previously worked on a RAG-based SaaS document management platform, but the strongest contribution was backend/cloud infrastructure, CI/CD, deployment, monitoring, and operations.

The current learning gap is:

```text
I have used RAG systems,
but I have not deeply understood retrieval quality, chunking behavior, embedding limitations, and evaluation.
```

This project helps move from:

```text
The RAG system seems to work.
```

to:

```text
The RAG system retrieved the expected source documents for specific test questions.
```

Korean note:

```text
이 프로젝트의 목적은 거대한 평가 프레임워크를 만드는 것이 아니라,
내 RAG 시스템의 검색 품질을 감으로 판단하지 않고 최소한의 기준으로 측정하는 것이다.
```

---

## 3. Relationship With Main Project

Main project:

```text
multi-agent-rag-assistant
```

Main project responsibility:

```text
Markdown documents
→ ingest
→ chunk
→ embedding
→ pgvector
→ retrieve
→ answer generation
→ later Planner / Evaluator / Retry nodes
```

This project responsibility:

```text
Send predefined questions to the local RAG API
and check whether expected source documents appear in retrieved results.
```

Important rule:

```text
This project should call the main project through HTTP API only.
Do not import code from the main RAG project.
```

---

## 4. Current Strategy

Build this project in phases.

### Phase 1: RAG Eval Harness

```text
YAML dataset
HTTP API call
Hit@K
Rich table
Markdown report
```

### Phase 2: Better Retrieval Evaluation

Possible later features:

```text
Hit@1 / Hit@3 / Hit@5
MRR
keyword matching
retrieval failure summary
```

### Phase 3: Agent Trace Viewer

After the main project has LangGraph nodes such as:

```text
Planner
Retriever
Generator
Evaluator
Retry
```

this project may evolve toward:

```text
rag-agent-observability-lab
```

or:

```text
agent-trace-viewer
```

But do not implement tracing in v1.

---

## 5. First Request For Codex

If you understand this context, reply:

```text
Context confirmed.
```

Then wait for the next task.
