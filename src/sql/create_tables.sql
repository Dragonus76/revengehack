CREATE TABLE targets (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    net_worth REAL NOT NULL,
    email TEXT,
    phone_number TEXT,
    is_compromised BOOLEAN DEFAULT FALSE
);

CREATE TABLE banks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    country TEXT NOT NULL
);

CREATE TABLE bank_accounts (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    account_number TEXT NOT NULL,
    decrypted_password TEXT,
    target_id INTEGER,
    bank_id INTEGER,
    FOREIGN KEY (target_id) REFERENCES targets (id),
    FOREIGN KEY (bank_id) REFERENCES banks (id)
);
