# Project Context

This document explains why `rag-eval-harness` exists and how to explain it to the developer.

---

## 1. Developer Context

The developer is a junior backend developer returning after a gap period.

Strong areas:

```text
FastAPI
PostgreSQL
Docker
AWS
CI/CD
backend infrastructure
monitoring
```

Current learning areas:

```text
RAG internals
retrieval quality tuning
embedding behavior
chunking strategy
LLM orchestration
multi-agent workflows
LangGraph
AI-assisted development
```

The developer understands backend and DevOps concepts faster than abstract ML concepts.

Helpful analogies:

```text
RAG evaluation is like a health check or monitoring probe for retrieval quality.
Agent tracing is like lightweight CloudWatch/X-Ray for LangGraph nodes.
Hit@K is like checking whether the expected service appears in the top K search results.
```

---

## 2. Main Learning Goal

The developer previously participated in a RAG-based SaaS project but did not gain enough hands-on understanding of RAG quality.

The key learning goal is:

```text
Do not just build a RAG system.
Learn how to judge whether retrieval is working correctly.
```

This project should help the developer answer:

```text
Did the retriever fetch the document I expected?
If not, was the issue caused by chunking, embedding, query wording, top_k, or source data?
```

---

## 3. Project Role

`rag-eval-harness` is not the main RAG system.

It is a companion evaluation tool for:

```text
multi-agent-rag-assistant
```

Good framing:

```text
The main project builds the RAG system.
This project measures whether retrieval behaves as expected.
```

Bad framing:

```text
This project is a replacement for the main RAG system.
This project judges final LLM answer quality.
This project compares Claude Code and Codex.
```

---

## 4. Response Style

Respond in Korean.

When explaining implementation decisions, keep explanations short and practical.

Before code, explain:

1. Why this structure is used
2. One simpler or alternative approach
3. Tradeoffs
4. Core concept the developer should understand

Do not over-explain theory unless the user asks.
