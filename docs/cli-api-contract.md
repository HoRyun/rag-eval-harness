# CLI and API Contract

This document defines the expected CLI behavior and local RAG API interaction.

---

## 1. Primary CLI Command

Primary command:

```bash
rag-eval run \
  --dataset eval/questions.yaml \
  --api-url http://localhost:8000 \
  --endpoint /retrieve \
  --top-k 3
```

The endpoint must be configurable.

The main RAG project may expose `/chat` before it exposes `/retrieve`.

Therefore this should also work:

```bash
rag-eval run \
  --dataset eval/questions.yaml \
  --api-url http://localhost:8000 \
  --endpoint /chat \
  --top-k 3
```

Do not hard-code `/retrieve`.

---

## 2. CLI Options

Recommended v1 options:

```text
--dataset   Path to YAML evaluation dataset
--api-url   Base URL of local RAG API
--endpoint  Endpoint path, such as /retrieve or /chat
--top-k     Number of retrieved sources to evaluate
--report    Optional Markdown report output path
```

Default values can be:

```text
--dataset eval/questions.yaml
--api-url http://localhost:8000
--endpoint /retrieve
--top-k 3
--report reports/latest.md
```

---

## 3. Request Shape

The main RAG API may evolve.

For v1, keep the request simple.

Recommended payload:

```json
{
  "question": "What is the v1 goal?",
  "top_k": 3
}
```

If the main project expects `query` instead of `question`, update only the client layer.

Keep request-building logic in:

```text
rag_eval/client.py
```

---

## 4. Internal Response Shape

The actual API response may differ.

Normalize all responses into this internal shape:

```python
{
    "sources": [
        {
            "source_path": "docs/PRD.md",
            "chunk_index": 0,
            "score": 0.12,
            "content": "..."
        }
    ]
}
```

Only `source_path` is required for Hit@K.

Other fields can be optional:

```text
chunk_index
score
content
```

---

## 5. Response Normalization Rule

Keep all response parsing and normalization inside:

```text
rag_eval/client.py
```

Do not spread parsing logic across modules.

WHY:

```text
The main RAG API is still evolving, so only one file should need to change when the response format changes.
```

---

## 6. Possible Source Field Names

The client may need to support common response shapes such as:

```json
{
  "sources": [
    {"source_path": "docs/PRD.md"}
  ]
}
```

```json
{
  "documents": [
    {"source_path": "docs/PRD.md"}
  ]
}
```

```json
{
  "retrieved_chunks": [
    {"source_path": "docs/PRD.md"}
  ]
}
```

Keep this logic simple and easy to edit.
