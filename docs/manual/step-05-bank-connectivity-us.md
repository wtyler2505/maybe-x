# STEP 5 — Bank connectivity (US)


**Plaid**: Link token → public_token → access_token (encrypted). Use `/transactions/sync` with cursor + webhooks.  
**SimpleFIN**: store key; poll `/accounts` & `/transactions`.  
Both normalize to internal schema and compute `hash_id`.


---
[Back to main manual](./maybe-x_consolidation_manual.md)
