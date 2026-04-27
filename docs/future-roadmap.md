# Future Roadmap

This document lists possible future directions.

Do not implement these in v1 unless the user explicitly asks.

---

## 1. v1: RAG Eval Harness

Current target:

```text
YAML dataset
HTTP API call
Hit@K
Rich table
Markdown report
```

This is the only required scope at the beginning.

---

## 2. v2: Better Retrieval Metrics

Possible additions:

```text
Hit@1 / Hit@3 / Hit@5
MRR
keyword presence check
per-source failure summary
latency summary
JSON report output
```

Only add these after v1 works.

---

## 3. v3: Agent Trace Viewer

Once the main project has LangGraph nodes such as:

```text
Planner
Retriever
Generator
Evaluator
Retry
```

this project may evolve into:

```text
agent-trace-viewer
```

or:

```text
rag-agent-observability-lab
```

---

## 4. Possible Trace Format

Future trace event example:

```json
{
  "run_id": "2026-04-27-001",
  "node": "retrieve",
  "input": {
    "query": "Explain Day 2 ingest flow"
  },
  "output": {
    "sources": ["docs/journal.md", "docs/PRD.md"]
  },
  "latency_ms": 421,
  "status": "success"
}
```

Do not implement this in v1.

---

## 5. Why Agent Trace Comes Later

Agent tracing needs actual agent execution flow.

If built too early, it becomes a fake JSON viewer with little learning value.

It becomes meaningful after the main project has:

```text
Planner node
Retriever node
Generator node
Evaluator node
Retry logic
```

---

## 6. Future Scope Control

When discussing future features, classify them as:

```text
Now
Later
Not needed
```

Default to `Later` unless the current v1 is already working.
