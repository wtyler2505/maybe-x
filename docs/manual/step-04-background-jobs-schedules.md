# STEP 4 — Background jobs & schedules


Workers: BankSync, FileImport, OCRIngest, Categorize, PriceFetch, Forecast, EmailIngest, EmbeddingBackfill.
Cron (dev): transactions every 15m; categorization every 10m; prices nightly; email every 5m.
Idempotency: always upsert by `hash_id`.


---
[Back to main manual](./maybe-x_consolidation_manual.md)
