import sqlite3 

conn = sqlite3.connect('bank.db')

c = conn.cursor()
c.execute("""
CREATE TABLE users (
    id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    name varchar(100) NOT NULL,
    agency varchar(10) NOT NULL,
    account varchar(20) NOT NULL,
    password varchar(20) NOT NULL,
    balance varchar(255) NOT NULL
    );
""")

print("User table created ! ")

c.close()
