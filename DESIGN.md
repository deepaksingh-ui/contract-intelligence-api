# Design (condensed)

Architecture: FastAPI + SQLite + TF-IDF retriever + rule-based extractor.

Data model: Document(id, filename, text, pages_json, uploaded_at)

Chunking: page-level chunks; max 2000 chars per chunk; rationale: pages preserve clause boundaries and keep TF-IDF effective.

Fallback behavior: if retriever fails, return full doc text and indicate low confidence.

Security notes: do not store PII in logs, limit upload size, run virus scan in production, enable auth (JWT) for endpoints.

Tradeoffs: no external LLM used to keep offline & self-contained; accuracy lower than fine-tuned model; easy to extend to embedding-based retriever (sentence-transformers) or call OpenAI/Azure.
