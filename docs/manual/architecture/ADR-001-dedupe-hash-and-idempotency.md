# ADR-001 — Dedupe Hash & Idempotency

Compute `hash_id = SHA256(user|date|amount|counterparty|fitid)` and upsert to prevent duplicates across all ingestion paths.

_Adopted 2025-08-16 03:06 UTC_
