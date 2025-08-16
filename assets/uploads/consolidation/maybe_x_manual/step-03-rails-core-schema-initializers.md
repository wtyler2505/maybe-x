# STEP 3 — Rails core: schema & initializers


Enable `vector` extension; tables for `bank_connections`, `transactions`, `embeddings`, `rules`, `prices`.
Initializer `LLM` with `chat` and `embed` calling Ollama REST.
Add IVFFlat index: `CREATE INDEX idx_embeddings_vec ON embeddings USING ivfflat (vec vector_cosine_ops) WITH (lists = 100);`.


---
[Back to main manual](./maybe-x_consolidation_manual.md)
