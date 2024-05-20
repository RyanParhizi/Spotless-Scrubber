import sqlite3
from faker import Faker

# conn = sqlite3.connect('database.sqlite')
# cur = conn.cursor()

# cur.execute("""
# CREATE TABLE contacts (
#     ID INTEGER PRIMARY KEY,
#     firstname TEXT,
#     lastname TEXT,
#     phone TEXT,
#     email TEXT
# )""")

# conn.commit()
# conn.close()

def add_contact(conn, firstname, lastname, phone, email):
    cur = conn.cursor()
    cur.execute("SELECT MAX(ID) FROM contacts")
    max_id = cur.fetchone()[0]
    next_id = 1 if max_id is None else max_id + 1

    cur.execute("INSERT INTO contacts (ID, firstname, lastname, phone, email) VALUES (?, ?, ?, ?, ?)", (next_id, firstname, lastname, phone, email))
    conn.commit()

def fetch_all_contacts(conn):
    cur = conn.cursor()
    cur.execute("SELECT * FROM contacts")
    contacts = cur.fetchall()
    return contacts

def fetch_all_contact_emails(conn):
    cur = conn.cursor()
    cur.execute("SELECT email FROM contacts")
    emails = cur.fetchall() # This returns a list of tuples 
    return emails

def remove_contacts_by_ID(ID, conn):
    cur = conn.cursor()
    cur.execute("DELETE FROM contacts WHERE ID=?", (ID,))
    conn.commit()

# def add_fake_contact(NOC, conn):
#     fake = Faker()
#     for i in range(NOC):
#         name = fake.name()
#         email = fake.email()
#         phone = fake.phone_number()
#         first_name, last_name = name.split(' ', 1)
#         add_contact(first_name, last_name, phone, email, conn)
#     conn.commit()

# def reset_database(conn):
#     cur = conn.cursor()
#     cur.execute("DELETE FROM contacts")
#     cur.execute("UPDATE sqlite_sequence SET seq = 0 WHERE name = 'contacts'")
#     conn.commit()
    #cur.execute("VACUUM")  ???