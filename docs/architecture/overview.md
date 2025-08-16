# Architecture Overview

Stack
- Frontend: React (CRA), TailwindCSS, Axios
- Backend: FastAPI (ASGI), Motor (async MongoDB driver)
- Database: MongoDB (MONGO_URL from backend/.env)
- Process manager: supervisor (backend:8001, frontend:3000)

Ingress and Ports
- All requests with path prefix /api go to backend at 0.0.0.0:8001
- All other requests go to frontend at 0.0.0.0:3000
- Do NOT hardcode ports or URLs; always use env vars

Environment Variables
- Frontend: REACT_APP_BACKEND_URL (see frontend/.env). Always call `${REACT_APP_BACKEND_URL}/api/...`
- Backend: MONGO_URL, DB_NAME, CORS_ORIGINS (see backend/.env)

High-Level Data Flow (Status Checks)

Client (React) --axios--> `${REACT_APP_BACKEND_URL}/api/status`
  - POST { client_name } -> FastAPI router /api/status
  - Backend validates, assigns UUID, inserts into Mongo with _id set to UUID
  - GET /api/status returns list of documents with id mapped from _id

ASCII Diagram

[Browser]
   |  GET /, static assets
   v
[Frontend (3000)] --XHR--> [Ingress /api prefix] --proxy--> [Backend (8001)] --Mongo URL--> [MongoDB]

CORS
- Configured to allow origins from CORS_ORIGINS (comma-separated). Default is "*" in backend/.env.

Logging
- Standard Python logging configured at INFO. For run/debug, inspect supervisor logs.