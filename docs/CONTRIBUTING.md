# Contributing Guide

- Commit messages: Conventional Commits (feat:, fix:, docs:, chore:, refactor:, test:, ci:)
- Code style: Black + isort for Python, ESLint + Prettier for JS (already in package.json). 
- API design: All backend routes must live under /api. Frontend must use REACT_APP_BACKEND_URL and never hardcode ports.
- Database: Use UUID strings for IDs; when storing in Mongo set _id to that UUID and map back to id on read to avoid ObjectId JSON issues.
- Testing: Add pytest unit tests in tests/ and UI tests later in docs/manual/testing.