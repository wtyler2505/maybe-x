# STEP 2 — Boot the stack


Compose services: Postgres (pgvector), Redis, Rails app, Sidekiq, ofx-ingest, ocr-ml.
Healthchecks: use `pg_isready`, Sidekiq Web UI at `/sidekiq`.
Resources: Desktop → 4 CPU / 8GB RAM for smooth dev.


---
[Back to main manual](./maybe-x_consolidation_manual.md)
