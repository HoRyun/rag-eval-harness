# Coding Rules

This document defines coding style, dependency rules, and implementation principles.

---

## 1. Language and Style

Use Python 3.12.

Use:

```text
type hints
docstrings
small functions
clear names
simple control flow
```

Prefer readable code over clever code.

---

## 2. Dependencies

Allowed v1 dependencies:

```text
Typer
httpx
PyYAML
Rich
pytest
uv
```

Do not add new dependencies without a clear reason.

Before adding a dependency, consider whether the Python standard library is enough.

---

## 3. Comments

Use comments only when they explain why, not what.

Good:

```python
# WHY: Keep response normalization in one place because the main RAG API may change.
normalized = normalize_response(payload)
```

Bad:

```python
# Loop over items.
for item in items:
    ...
```

For important decisions, use `WHY:` comments.

---

## 4. Code Generation Explanation

Before generating code, briefly explain:

1. Why this structure is being used
2. One simpler or alternative approach
3. Tradeoffs
4. Core concept the developer should understand

Keep this explanation short.

The developer can overthink, so avoid long theoretical explanations.

---

## 5. Abstraction Rule

Prefer simple functions first.

Good:

```text
load_dataset()
call_rag_api()
normalize_response()
evaluate_case()
render_markdown_report()
```

Avoid in v1:

```text
plugin system
strategy pattern
repository layer
service container
factory registry
abstract base classes
```

---

## 6. File Size Rule

If a file grows beyond 300 lines, consider splitting it.

Do not split files prematurely.

---

## 7. CLI Implementation Rule

Use Typer for CLI commands.

Keep CLI orchestration in:

```text
rag_eval/main.py
```

Move pure logic into:

```text
rag_eval/dataset.py
rag_eval/client.py
rag_eval/metrics.py
rag_eval/report.py
```

---

## 8. Response Language Rule

Respond to the developer in Korean.

Use English for:

```text
code
function names
class names
docstrings
README structure
configuration files
```

Use Korean comments only for important design reasoning.
