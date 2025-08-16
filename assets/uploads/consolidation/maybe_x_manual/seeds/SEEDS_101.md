# Seeds 101 — What “model names” means (and how to adapt)

In Rails, a **model** is a Ruby class backed by a table (e.g., `Transaction`, `Account`, `User`). Different forks name these classes and columns slightly differently. For example:
- The transaction model might be called `Transaction`, `Txn`, `Entry`, or `Posting`.
- The amount column might be `amount` (decimal) or `amount_cents` (Money gem).
- The merchant might be `counterparty`, `merchant`, `payee`, or `description`.

To make seeds work no matter what you named things, use the **Smart Seeds** script included here. It **auto-detects** common model/column names, and you can override anything with a tiny YAML mapping file.

## TL;DR
- If your app uses `User`, `Account`, and `Transaction` with columns `date`, `amount` or `amount_cents`, `currency`, `counterparty`/`description`, `memo`, `fitid`, `account_id`, `user_id`, you’re good—run the seeds.
- If you named them differently, edit `db/seeds_mapping.yml` (explained below) or just rename keys in the seed template.

## How the Smart Seeds decide what to use
1. **Model class**: tries a list of common names and picks the first that exists and is an ActiveRecord model.
2. **Column names**: checks the model’s `column_names` and picks the closest match from a candidate list.
3. **Foreign keys**: looks for `account_id` and `user_id` variants.
4. **Amounts**: writes to `amount_cents` if present, else to `amount`.

## Mapping file (optional overrides)
Create `db/seeds_mapping.yml` to force specific choices:
```yaml
models:
  user: User
  account: Account
  transaction: Transaction
columns:
  transaction:
    date: posted_on
    amount: amount_cents
    currency: currency_code
    counterparty: merchant
    memo: note
    fitid: external_id
    account_fk: ledger_account_id
    user_fk: user_id
defaults:
  user:
    email: demo@example.com
    password: password
  account:
    name: Checking
    currency: USD
```

## Running
```bash
bin/rails db:prepare
bin/rails runner db/smart_seeds.rb     # imports db/fixtures/transactions.csv by default
```
_Last updated 2025-08-16 03:16 UTC_