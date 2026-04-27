# Testing and Error Handling

This document defines test priorities and beginner-friendly error handling rules.

---

## 1. Testing Priority

Prioritize tests for pure logic.

Test first:

```text
dataset loading
dataset validation
Hit@K calculation
Markdown report rendering
response normalization with sample payloads
```

Do not require a running RAG server for unit tests.

HTTP integration tests can be added later.

---

## 2. Recommended Test Files

```text
tests/test_dataset.py
tests/test_metrics.py
tests/test_report.py
```

Optional later:

```text
tests/test_client.py
```

Use sample payloads instead of a real server where possible.

---

## 3. Dataset Validation Cases

Test these cases:

```text
valid dataset
missing cases key
case missing id
case missing question
case missing expected_sources
case missing expected_keywords
expected_sources is not a list
expected_keywords is not a list
empty cases list
```

---

## 4. Metric Test Cases

Test these cases:

```text
expected source appears at rank 1
expected source appears within top_k
expected source appears after top_k
expected source does not appear
multiple expected sources
no retrieved sources
path normalization with ./ prefix
path normalization with backslashes
```

---

## 5. Error Handling Cases

Handle these clearly:

```text
dataset file not found
invalid YAML
missing required fields
API connection failure
API returns non-200 status
API response cannot be normalized
no sources returned
```

---

## 6. Error Message Style

Error messages should help a beginner fix the problem.

Bad:

```text
KeyError: sources
```

Good:

```text
Could not find retrieved sources in the API response.
Check rag_eval/client.py response normalization logic.
```

Bad:

```text
ConnectionError
```

Good:

```text
Could not connect to the RAG API at http://localhost:8000.
Make sure the main RAG server is running.
```

---

## 7. Integration Test Rule

Do not make unit tests depend on a running RAG server.

If integration tests are added later, mark them separately or document that they require the local server.
