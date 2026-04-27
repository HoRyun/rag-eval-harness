# Architecture

This document defines the recommended project structure and module responsibilities.

---

## 1. Design Principle

Keep the architecture boring and easy to explain.

Good:

```text
load dataset
call API
evaluate result
print table
write report
```

Avoid:

```text
framework design
plugin system
repository layer
database abstraction
async task queue
web dashboard
```

---

## 2. Recommended Project Structure

Use this structure unless the user asks otherwise:

```text
rag-eval-harness/
├─ pyproject.toml
├─ README.md
├─ HANDOFF.md
├─ CODEX.md
├─ eval/
│  └─ questions.yaml
├─ reports/
│  └─ .gitkeep
├─ docs/
│  └─ codex/
│     ├─ project-context.md
│     ├─ scope.md
│     ├─ architecture.md
│     ├─ cli-api-contract.md
│     ├─ evaluation-rules.md
│     ├─ coding-rules.md
│     ├─ testing-error-handling.md
│     └─ future-roadmap.md
├─ rag_eval/
│  ├─ __init__.py
│  ├─ main.py
│  ├─ dataset.py
│  ├─ client.py
│  ├─ metrics.py
│  └─ report.py
└─ tests/
   ├─ test_dataset.py
   ├─ test_metrics.py
   └─ test_report.py
```

---

## 3. Module Responsibilities

### `rag_eval/main.py`

CLI entrypoint.

Responsibilities:

```text
Define Typer app
Parse CLI options
Coordinate dataset loading, API call, evaluation, table output, report output
```

Do not put metric or parsing logic here.

---

### `rag_eval/dataset.py`

Dataset loading and validation.

Responsibilities:

```text
Read YAML file
Validate required fields
Return typed evaluation cases
```

---

### `rag_eval/client.py`

HTTP API client and response normalization.

Responsibilities:

```text
Call local RAG API
Handle HTTP errors
Normalize API response into internal source shape
```

Keep response parsing here because the main RAG API may change.

---

### `rag_eval/metrics.py`

Evaluation logic.

Responsibilities:

```text
Calculate Hit@K
Find rank of first expected source
Return per-case evaluation result
```

This module should be easy to unit test without a running server.

---

### `rag_eval/report.py`

Output rendering.

Responsibilities:

```text
Render Markdown report
Optionally help format summary data
```

Rich table rendering can be in `main.py` or a small helper if needed.

---

## 4. External Boundary Rule

Do not import code from the main RAG project.

Good:

```text
rag-eval-harness → HTTP request → local RAG API
```

Bad:

```text
from app.rag.retrieve import retrieve
```

WHY:

```text
This project should behave like an external evaluation/monitoring probe, not an internal module.
```
