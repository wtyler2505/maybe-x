# Testing Guide

Manual API Tests (curl)
- Hello: curl -sS ${BACKEND}/api/
- Health: curl -sS ${BACKEND}/api/health
- Create: curl -sS -X POST ${BACKEND}/api/status -H 'Content-Type: application/json' -d '{"client_name": "tester"}'
- List: curl -sS ${BACKEND}/api/status

Note: ${BACKEND} equals the value of REACT_APP_BACKEND_URL.

UI Manual Test
- Load frontend root in browser
- Expect to see: logo, "Building something incredible ~!", Hello message, Health status
- Enter a client name, click Create Status, and see it appear in the list with timestamp

Automated Testing Plan
- Backend: add pytest with httpx/starlette TestClient. Use ENV to point to test DB or a mocked layer. Validate 200 responses and schema.
- Frontend: Playwright tests to validate page load, health status visible, form submission, and list updated. Prefer data-testid attributes for robust selectors.

Troubleshooting
- If API fails from UI, check browser console, Network tab: requests must be `${REACT_APP_BACKEND_URL}/api/...`
- Inspect backend logs: tail -n 100 /var/log/supervisor/backend.*.log