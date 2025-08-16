# Integrations

Before integrating any third-party services, prepare required API keys and place them in appropriate .env files. Always prefix backend routes with /api and never hardcode external URLs. For detailed playbooks, engage the integration_playbook_expert when needed.

Candidate Integrations
- Email/SMS (SendGrid/Twilio)
- Bank connectivity (Plaid)
- File storage (S3-compatible)
- LLM providers via Emergent Integrations (OpenAI/Anthropic/Google)

Note: Ask the user for keys before implementing any integration.