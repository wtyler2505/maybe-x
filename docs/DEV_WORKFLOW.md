# Developer Workflow

Prerequisites
- Python 3.10+
- Node.js 20+ and Yarn (already configured)
- MongoDB accessible via backend/.env MONGO_URL

Install
- Backend: pip install -r backend/requirements.txt
- Frontend: yarn --cwd frontend install

Run (managed by supervisor)
- Restart everything: sudo supervisorctl restart all
- Check status: sudo supervisorctl status

Logs
- Backend: tail -n 100 /var/log/supervisor/backend.*.log
- Frontend: tail -n 100 /var/log/supervisor/frontend.*.log

Environment Rules
- Do NOT edit frontend/.env REACT_APP_BACKEND_URL or backend/.env MONGO_URL/DB_NAME/ports
- Frontend uses process.env.REACT_APP_BACKEND_URL; backend attaches all routes to /api

Coding Standards
- Backend: Pydantic models, small routers, UUIDs for IDs, explicit _id mapping
- Frontend: Centralized API client in src/api.js, no hardcoded URLs, error handling at the boundary

Typical Dev Loop
1) Edit backend or frontend code
2) Save – hot reload usually applies
3) If you changed requirements or .env, run: sudo supervisorctl restart backend or frontend
4) Verify via curl and UI