# STEP 1 — Secrets & environment


Create `.env`:
```
RAILS_ENV=development
SECRET_KEY_BASE=...
DATABASE_URL=postgres://user:pass@localhost:5432/maybe_x_dev
REDIS_URL=redis://localhost:6379/0
ENABLE_PLAID=true
ENABLE_SIMPLEFIN=true
ENABLE_OCR=true
ENABLE_LLM=true
ENABLE_EMAIL_INGEST=true
PLAID_CLIENT_ID=...  PLAID_SECRET=... PLAID_ENV=sandbox
SIMPLEFIN_BRIDGE_BASE=https://beta-bridge.simplefin.org
OLLAMA_BASE=http://localhost:11434
LLM_CHAT_MODEL=llama3.1:8b
EMBED_MODEL=nomic-embed-text
OCR_URL=http://localhost:8082
```
Security: never commit `.env`; encrypt `bank_connections.auth` using Rails encrypted attributes or Lockbox.


---
[Back to main manual](./maybe-x_consolidation_manual.md)
