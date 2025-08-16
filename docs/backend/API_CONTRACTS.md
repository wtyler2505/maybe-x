# Backend API Contracts

Base URL
- `${REACT_APP_BACKEND_URL}/api`

Health
- GET `/` → 200 OK
  - Response: { "message": "Hello World" }
- GET `/health` → 200 OK
  - Response: { "status": "ok" }

Status Checks
- POST `/status` → 200 OK
  - Request: { "client_name": string }
  - Response: { "id": uuid, "client_name": string, "timestamp": ISO8601 }
- GET `/status` → 200 OK
  - Response: [ { "id": uuid, "client_name": string, "timestamp": ISO8601 }, ... ]

Error Format
- 4xx/5xx → { "detail": string }

Notes
- IDs are UUID strings. In Mongo, we store them as `_id` to avoid ObjectId serialization issues. On reads, `_id` is mapped back to `id`.
- All endpoints are under `/api` to satisfy ingress rules.