import sqlite3
import sys

db_conn = sqlite3.connect('Coursework.db')

with db_conn:
    
    cur = db_conn.cursor()    
    cur.execute("SELECT * FROM Users",)

    row = cur.fetchall()
    for a in row:
        print (a)
db_conn.close()
