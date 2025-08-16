# STEP 0 — One-time prerequisites (Windows friendly)


- Enable WSL2 + Virtual Machine Platform. Install Ubuntu 22.04.
- Install: `git curl build-essential libpq-dev libssl-dev zlib1g-dev imagemagick poppler-utils tesseract-ocr`.
- `sudo apt install postgresql postgresql-contrib redis`.
- Local LLM: `ollama pull llama3.1:8b nomic-embed-text && ollama serve &`.
- Docker Desktop alternative: use `ops/docker/docker-compose.yml`.


---
[Back to main manual](./maybe-x_consolidation_manual.md)
