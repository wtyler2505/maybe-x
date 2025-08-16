# Ops Runbooks

API Down (5xx)
- Check backend logs
- Verify MONGO_URL is reachable
- GET /api/health returns ok? If not, fix Mongo connectivity

Frontend Not Loading
- Check frontend logs
- Ensure build dependencies are installed: yarn --cwd frontend install

CORS Issues
- CORS_ORIGINS in backend/.env should include your domain(s). Restart backend after changes.

Ingress Misrouting
- Ensure all backend API calls are prefixed with /api. Non-/api calls go to frontend.

Performance
- Add Mongo indices as needed (timestamp on status_checks).

Data Safety
- UUIDs avoid ObjectId serialization issues. Do not switch to ObjectIds.