# Database Schema

MongoDB
- Connection string: `MONGO_URL` from backend/.env (default: mongodb://localhost:27017)
- Database name: `DB_NAME` from backend/.env (default: test_database)

Collections
- status_checks
  - _id: string (UUID v4)
  - client_name: string
  - timestamp: Date (UTC)

Indexes (optional, recommended for scale)
- status_checks: index on timestamp (descending)

Conventions
- Always use UUID strings for identifiers and set them as `_id` to avoid ObjectId JSON issues.
- Timestamps are stored in UTC using datetime.utcnow on the server.

Connectivity Test
- Use GET /api/health to verify Mongo connectivity.