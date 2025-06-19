# just an algorithm to make it easier for me to keep track of my cash form my server postiion
'''import sqlite3
import datetime
import os

db = "server_cash.db"

def initialize_db():
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(
                   CREATE TABLE IF NOT EXISTS earnings (
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   entry_date TEXT NOT NULL UNIQUE,
                   weekly_earnings REAL NOT NULL,
                   total REAL NOT NULL
    )
)
    conn.commit()
    conn.close()
'''
#calculation of money from each bill. 
def counter(single, fives, tens, twenties, fifties, hundreds):
    amount_for_fives = fives * 5
    amount_for_tens = tens * 10
    amount_for_twenties = twenties * 20
    amount_for_fifties = fifties * 50
    amount_for_hundreds = hundreds * 100

    total = amount_for_fives + amount_for_tens + amount_for_twenties + amount_for_fifties + amount_for_hundreds + single 

    return total 


