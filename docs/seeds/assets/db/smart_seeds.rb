
# db/smart_seeds.rb — auto-detecting seed importer
# Usage: bin/rails runner db/smart_seeds.rb [path_to_csv]
require "csv"
require "digest"
require "yaml"

def pick_model(*candidates)
  candidates.each do |const|
    begin
      klass = Object.const_get(const.to_s)
      return klass if klass.respond_to?(:ancestors) && klass.ancestors.map(&:to_s).include?("ActiveRecord::Base")
    rescue NameError
    end
  end
  nil
end

def first_present(cols, *cands)
  cands.map(&:to_s).find { |c| cols.include?(c) }
end

def load_mapping
  path = Rails.root.join("db", "seeds_mapping.yml")
  return {} unless File.exist?(path)
  YAML.load_file(path) || {}
end

def symbol_hash(h)
  Hash[h.map { |k, v| [k.to_sym, v.is_a?(Hash) ? symbol_hash(v) : v] }]
end

map = symbol_hash(load_mapping)

UserModel  = (map.dig(:models, :user)&.constantize rescue nil) ||
             pick_model(:User, :AccountUser, :Member, :Person)
AccountModel = (map.dig(:models, :account)&.constantize rescue nil) ||
               pick_model(:Account, :FinancialAccount, :LedgerAccount, :Wallet)
TxnModel   = (map.dig(:models, :transaction)&.constantize rescue nil) ||
             pick_model(:Transaction, :Txn, :Entry, :Posting, :LedgerEntry, :Movement)

raise "SmartSeeds: could not find a Transaction-like model (Transaction/Txn/Entry/Posting...)" unless TxnModel

txn_cols = TxnModel.column_names.map(&:to_s)

TXN_DATE    = map.dig(:columns, :transaction, :date)&.to_s ||
              first_present(txn_cols, :date, :posted_on, :booked_on, :transaction_date)
TXN_AMOUNT  = map.dig(:columns, :transaction, :amount)&.to_s ||
              first_present(txn_cols, :amount_cents, :amount, :value_cents, :value)
TXN_CCY     = map.dig(:columns, :transaction, :currency)&.to_s ||
              first_present(txn_cols, :currency, :currency_code)
TXN_CP      = map.dig(:columns, :transaction, :counterparty)&.to_s ||
              first_present(txn_cols, :counterparty, :merchant, :payee, :description, :name)
TXN_MEMO    = map.dig(:columns, :transaction, :memo)&.to_s ||
              first_present(txn_cols, :memo, :note, :description)
TXN_FITID   = map.dig(:columns, :transaction, :fitid)&.to_s ||
              first_present(txn_cols, :fitid, :external_id, :import_uid, :source_id, :provider_id)

TXN_ACCOUNT_FK = map.dig(:columns, :transaction, :account_fk)&.to_s ||
                 first_present(txn_cols, :account_id, :financial_account_id, :ledger_account_id, :wallet_id)
TXN_USER_FK    = map.dig(:columns, :transaction, :user_fk)&.to_s ||
                 first_present(txn_cols, :user_id, :account_user_id, :member_id, :person_id)

raise "SmartSeeds: missing a date-like column on #{TxnModel} (looked for date/posted_on/...)" unless TXN_DATE
raise "SmartSeeds: missing an amount/amount_cents-like column on #{TxnModel}" unless TXN_AMOUNT

defaults_user   = map.dig(:defaults, :user)   || { "email"=>"demo@example.com", "password"=>"password" }
defaults_acct   = map.dig(:defaults, :account)|| { "name"=>"Checking", "currency"=>"USD" }

user = nil
if UserModel
  user = UserModel.first || UserModel.create!(**defaults_user.transform_keys(&:to_sym))
end

account = nil
if AccountModel
  attrs = defaults_acct.transform_keys(&:to_sym)
  # attach user_id if the account has that column
  if user && AccountModel.column_names.include?("user_id")
    attrs[:user_id] = user.id
  end
  account = AccountModel.first || AccountModel.create!(attrs.select { |k,_| AccountModel.column_names.include?(k.to_s) })
end

csv_path = ARGV[0] || Rails.root.join("db", "fixtures", "transactions.csv").to_s
abort "SmartSeeds: CSV not found at #{csv_path}" unless File.exist?(csv_path)

puts "SmartSeeds: importing #{csv_path} into #{TxnModel}"
count = 0

CSV.foreach(csv_path, headers: true) do |r|
  date_str = r["Date"] || r["TransactionDate"] || r["Posted"] || r["Posting Date"]
  date = Date.parse(date_str.to_s) rescue nil
  next unless date

  amount = if r["Amount"] && !r["Amount"].empty?
    r["Amount"].to_f
  else
    (r["Debit"].to_f) - (r["Credit"].to_f)
  end

  counterparty = (r["Description"] || r["Merchant"] || r["Payee"]).to_s.strip
  memo = (r["Memo"] || "").to_s.strip
  fitid = (r["TransactionId"] || r["FITID"] || "").to_s.strip

  attrs = {}
  attrs[TXN_DATE.to_sym] = date
  if TXN_AMOUNT == "amount_cents" || TXN_AMOUNT == "value_cents"
    attrs[TXN_AMOUNT.to_sym] = (amount * 100).round
  else
    attrs[TXN_AMOUNT.to_sym] = amount
  end
  attrs[TXN_CCY.to_sym] = "USD" if TXN_CCY && TxnModel.column_names.include?(TXN_CCY) && !attrs.key?(TXN_CCY.to_sym)
  attrs[TXN_CP.to_sym]  = counterparty if TXN_CP && TxnModel.column_names.include?(TXN_CP)
  attrs[TXN_MEMO.to_sym]= memo if TXN_MEMO && TxnModel.column_names.include?(TXN_MEMO)
  attrs[TXN_FITID.to_sym]= fitid if TXN_FITID && TxnModel.column_names.include?(TXN_FITID)

  if account && TXN_ACCOUNT_FK && TxnModel.column_names.include?(TXN_ACCOUNT_FK)
    attrs[TXN_ACCOUNT_FK.to_sym] = account.id
  end
  if user && TXN_USER_FK && TxnModel.column_names.include?(TXN_USER_FK)
    attrs[TXN_USER_FK.to_sym] = user.id
  end

  key_parts = [user&.id, account&.id, date, amount, counterparty, fitid].compact
  hash_id = Digest::SHA256.hexdigest(key_parts.join("|"))
  exists = if TxnModel.column_names.include?("hash_id")
    TxnModel.where(hash_id: hash_id).exists?
  else
    TxnModel.where(TXN_DATE => date, TXN_AMOUNT => attrs[TXN_AMOUNT.to_sym]).exists?
  end
  next if exists

  TxnModel.create!(attrs)
  count += 1
end

puts "SmartSeeds: imported #{count} transactions"
