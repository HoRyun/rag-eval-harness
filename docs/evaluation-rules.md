# Evaluation Rules

This document defines dataset format and v1 evaluation logic.

---

## 1. Dataset Format

Use YAML.

Expected shape:

```yaml
cases:
  - id: q001
    question: "What is the v1 goal of the main RAG project?"
    expected_sources:
      - "docs/PRD.md"
    expected_keywords:
      - "ingest"
      - "chat"
      - "FastAPI"
```

Required fields:

```text
id
question
expected_sources
expected_keywords
```

---

## 2. Field Meaning

### `id`

Stable case identifier.

Example:

```text
q001
```

### `question`

Question sent to the local RAG API.

### `expected_sources`

Source paths expected to appear in retrieved results.

Example:

```text
docs/PRD.md
docs/decision-log.md
docs/journal.md
```

### `expected_keywords`

Keywords that may be useful later.

In v1:

```text
Load this field.
Validate this field.
Include it in the dataset model if useful.
Do not use it for complex answer scoring yet.
```

---

## 3. v1 Metric: Hit@K

Use Hit@K only.

Definition:

```text
A case passes if at least one expected_source appears in the top K retrieved sources.
```

Example:

```text
expected_sources:
  - docs/PRD.md

retrieved sources:
  1. docs/HANDOFF.md
  2. docs/PRD.md
  3. docs/journal.md

Hit@3 = true
Rank = 2
```

---

## 4. Result Fields

Each evaluated case should produce at least:

```text
case_id
question
passed
rank
expected_sources
retrieved_sources
top_k
```

Optional fields:

```text
error
latency_ms
```

Do not add complex scoring in v1.

---

## 5. Matching Rule

Use exact source path match in v1.

Example:

```text
expected_source: docs/PRD.md
retrieved_source: docs/PRD.md
match: true
```

Be careful with path normalization.

Reasonable normalization:

```text
strip leading ./
normalize backslashes to forward slashes
strip surrounding whitespace
```

Do not implement fuzzy matching unless requested.

---

## 6. Summary Output

The CLI should summarize:

```text
total cases
passed cases
failed cases
top-k
pass rate
```

Example:

```text
Total: 5
Passed: 4
Failed: 1
Hit@3: 80.0%
```

---

## 7. What This Does Not Evaluate

This v1 metric does not evaluate:

```text
final answer correctness
answer fluency
faithfulness
hallucination
LLM reasoning quality
```

It only evaluates:

```text
whether expected source documents appeared in retrieved results
```
