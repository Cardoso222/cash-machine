import sqlite3

conn = sqlite3.connect('bank.db')

c = conn.cursor()
c.execute("""
        INSERT INTO users (name, agency, account, password, balance) VALUES ('jonh doe', '1234', '1010', '123', '200') 
        """)

conn.commit()

print('success !') 

c.close()
