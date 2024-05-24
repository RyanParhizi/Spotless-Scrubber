import sqlite3

conn = sqlite3.connect('database.sqlite')
cur = conn.cursor()

cur.execute("""
CREATE TABLE contacts (
    ID INTEGER PRIMARY KEY,
    firstname TEXT,
    lastname TEXT,
    phone TEXT,
    email TEXT
)""")