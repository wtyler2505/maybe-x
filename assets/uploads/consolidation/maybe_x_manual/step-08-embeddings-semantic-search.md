# STEP 8 — Embeddings & semantic search


On ingest, embed semantic text for transactions/receipts/statements using Ollama embeddings; store in `embeddings(vec)`.
Similarity: `ORDER BY vec <-> $query LIMIT 25`. Add helper to convert arrays to pgvector literal.


---
[Back to main manual](./maybe-x_consolidation_manual.md)
