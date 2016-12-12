import sqlite3
import json

conn = sqlite3.connect('db/bank.db')
c = conn.cursor()


def getUserData(ag, acc, password):
    c.execute('SELECT * FROM users WHERE agency = ? and account = ? ',
            (ag, acc,)) 
    result = c.fetchone()
    if (result):
        return result
    return False 

def userExists(ag, acc):
    c.execute('SELECT * FROM users WHERE agency = ? and account = ? ',
            (ag, acc,)) 
    result = c.fetchone()
    if (result):
        return True
    return False 

def getUserName(ag, acc):
    c.execute('SELECT * FROM users WHERE agency = ? and account = ? ',
            (ag, acc,)) 
    result = c.fetchone()
    return result[1]

def getUserBalance(ag, acc):
    c.execute('SELECT * FROM users WHERE agency = ? and account = ?',
            (ag, acc,)) 
    result = c.fetchone()
    return result[5]

def userWithdrawal(ag, acc, value):
    balance = getUserBalance(ag, acc) - value
    c.execute('UPDATE users SET balance = ? WHERE agency = ? and account = ?',
            (balance, ag, acc,))

def userDeposit(ag, acc, value): 
    if(userExists(ag, acc) == True):

        balance = int(getUserBalance(ag, acc)) + value
        c.execute('UPDATE users SET balance = ? WHERE agency = ? and account = ?',
                (balance, ag, acc,))
        return True
    return False
