# Project Roadmap and Developer Guide

This repository is a full-stack application scaffold with:
- Backend: FastAPI running on 0.0.0.0:8001 with MongoDB
- Frontend: React (CRA + Tailwind + Radix UI) served on port 3000
- Database: MongoDB via MONGO_URL (see backend/.env)
- Supervisor: Manages backend and frontend processes

CRITICAL URL/ENV RULES
- Do not modify backend/.env or frontend/.env URLs or ports.
- Frontend must call the backend using process.env.REACT_APP_BACKEND_URL and prefix all API calls with /api.
- Backend must read Mongo using os.environ['MONGO_URL'] and expose routes under /api.

Quick Start
- Install Python deps: pip install -r backend/requirements.txt
- Install frontend deps: yarn --cwd frontend install
- Restart services via supervisor: sudo supervisorctl restart all

Docs
- See docs/manual for the Maybe-X consolidation manual and step-by-step guides.
- See docs/ for architecture, API contracts, DB schema, development workflow, testing, troubleshooting and runbooks.

High-level Features
- /api/ root returns { message: "Hello World" }
- /api/status supports POST + GET for status checks (UUID-based, JSON-serializable)

Contributing
- Please read docs/CONTRIBUTING.md and follow the coding standards, commit style, and PR guidelines.