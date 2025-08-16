# Documentation Index

Welcome to the project documentation. This app is a FastAPI + MongoDB backend with a React (CRA + Tailwind) frontend. Supervisor runs services in the background. All backend routes must be under /api and the frontend must use REACT_APP_BACKEND_URL to call the backend.

Table of Contents
- Architecture
  - docs/architecture/overview.md
- Backend
  - docs/backend/API_CONTRACTS.md
- Frontend
  - docs/frontend/README.md
- Database
  - docs/database/SCHEMA.md
- Testing
  - docs/testing/README.md
- Ops & Runbooks
  - docs/ops/RUNBOOKS.md
- Integrations
  - docs/integrations/README.md
- Developer Workflow
  - docs/DEV_WORKFLOW.md
- Roadmap
  - docs/ROADMAP.md
- Manual (Provided by your ZIPs)
  - docs/manual (step-by-step guides, ADRs, seeds, security, UI)

Key Rules Recap
- Do not modify .env values. Use environment variables, never hardcode URLs or ports.
- Frontend → Backend: process.env.REACT_APP_BACKEND_URL and prefix with /api
- Backend → MongoDB: os.environ['MONGO_URL']
- Kubernetes ingress routes /api to backend:8001 and all other paths to frontend:3000