# Frontend Guide

Stack
- React 19 (CRA), TailwindCSS, Axios

Key Rules
- Always read backend URL from process.env.REACT_APP_BACKEND_URL
- Always prefix with /api for backend routes

API Access
- Use src/api.js, which exports functions getHello, getHealth, createStatus, listStatus.

Local Dev Tips
- If API calls fail, check the value of REACT_APP_BACKEND_URL and ensure it points to the ingress that routes /api to backend.
- Do not hardcode URLs or ports.