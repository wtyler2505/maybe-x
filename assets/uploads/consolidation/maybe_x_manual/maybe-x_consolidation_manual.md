# Maybe-X (US-Only, Local-AI) — Consolidation & Wiring Manual

> Windows/WSL2 or Docker Desktop • Rails 7 • Postgres 16 + pgvector • Redis/Sidekiq • Node 20 • Python 3.11 • Local LLM (Ollama or llama.cpp)

## Quickstart
1. `git clone <your-fork> maybe-x && cd maybe-x`
2. `cp .env.example .env` → fill values (see Step 1).
3. Start deps: `docker compose -f ops/docker/docker-compose.yml up -d db redis`
4. Start LLM: `ollama pull llama3.1:8b nomic-embed-text && ollama serve &`
5. App: `cd apps/web && bundle install && yarn install && bin/rails db:prepare && bin/dev`
6. Visit http://localhost:3000 and verify status. Sidekiq at `/sidekiq`.

---

## Steps
0. One-time prerequisites (Windows friendly)  
1. Secrets & environment  
2. Boot the stack  
3. Rails core: schema & initializers  
4. Background jobs & schedules  
5. Bank connectivity (US)  
6. Importers (OFX/QIF/CSV)  
7. OCR, PII, and document intake  
8. Embeddings & semantic search  
9. Deterministic rules + ML fallback  
10. Forecasting & anomaly detection  
11. Market data & valuations  
12. Crypto balances (optional)  
13. Email/SMS → pending transactions  
14. Local LLM usage patterns (deep integration)  
15. UI surfaces you must add  
16. Developer workflow (fast path)  
17. Observability & safety nets  
18. Testing checklist  
19. Licensing & branding  
20. Ready-to-copy snippets  
21. Order of operations (follow this)  
22. Pitfalls & pro tips

---

## Companion Docs Index
- Integration Link Directory → `integrations/links.md`
- Architecture Decisions → `architecture/ADR-001-dedupe-hash-and-idempotency.md`, `architecture/ADR-002-embedding-store-and-similarity.md`, `architecture/ADR-003-llm-guardrails-json-schemas.md`
- Runbooks (Ops) → `ops/RUNBOOK-ingestion-failures.md`, `ops/RUNBOOK-ocr-service.md`, `ops/RUNBOOK-plaid-webhooks.md`, `ops/RUNBOOK-email-ingest.md`, `ops/RUNBOOK-forecasting-anomalies.md`
- Security & Privacy → `security/PII-Handling-Guide.md`, `security/Privacy-Local-AI-Mode.md`
- Testing → `testing/TESTPLAN.md`
- UI → `ui/Design-And-Accessibility.md`
- Migrations → `migrations/Migrate-From-YNAB-And-Actual.md`
- Glossary → `resources/GLOSSARY.md`

---

_Last updated: 2025-08-16 03:06 UTC_