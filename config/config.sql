/*
This table stores all transactions made through time.
transactID: A unique ID for each transaction.
opDay: The date when operation was made.
ammount: The cost/ammount of money involved in the transaction.
descr: A brief description of the operation.
cat: The category of the transaction.
type: The type of transaction (Income, cost, or movement of money between accounts).
payFrom: The account used for the operation.
payTo: Where the operation was made or where the money ends.
*/
CREATE TABLE IF NOT EXISTS transanction (
    transactID TEXT PRIMARY KEY,
    opDay TEXT NOT NULL,
    ammount REAL NOT NULL,
    descr TEXT NOT NULL,
    cat TEXT NOT NULL,
    type TEXT NOT NULL,
    payFrom  TEXT NOT NULL,
    payTo TEXT NOT NULL,
    FOREIGN KEY (cat) REFERENCES category (catID)
    ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (type) REFERENCES transactionType (transactID)
    ON DELETE CASCADE ON UPDATE NO ACTION,
    FOREIGN KEY (payFrom) REFERENCES accounts (accID)
    ON DELETE CASCADE ON UPDATE NO ACTION
);

CREATE TABLE IF NOT EXISTS category(
    catID TEXT PRIMARY KEY,
    descr TEXT
);

CREATE TABLE IF NOT EXISTS transactionType(
    transactTypeID TEXT PRIMARY KEY,
    descr TEXT
);

CREATE TABLE IF NOT EXISTS accounts(
    accID TEXT PRIMARY KEY,
    descr TEXT
);

CREATE TABLE IF NOT EXISTS accountHistory(
    transactID PRIMARY KEY,
    opDay TEXT NOT NULL,
    account TEXT NOT NULL,
    ammount REAL NOT NULL
);