from flask import Flask, render_template, request, redirect, url_for
import sqlite3
from database import add_contact, fetch_all_contacts, remove_contacts_by_ID

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/send")
def send():
    return render_template("send.html")

@app.route('/database', methods=['GET', 'POST'])
def database():
    if request.method == 'POST':
        action = request.form['action']
        if action == 'add':
            firstname = request.form['firstname']
            lastname = request.form['lastname']
            phone = request.form['phone']
            email = request.form['email']
            
            with sqlite3.connect('database.sqlite') as conn:
                add_contact(conn, firstname, lastname, phone, email)
                
        elif action == 'delete':
            contact_id = request.form['id']
            
            with sqlite3.connect('database.sqlite') as conn:
                remove_contacts_by_ID(contact_id, conn)
                
        return redirect(url_for('database'))

    with sqlite3.connect('database.sqlite') as conn:
        contacts = fetch_all_contacts(conn)

    return render_template("database.html", contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)

 
# app.route('/send', methods=['GET', 'POST'])
# def send():
#     if request.method == 'POST':
#         if request.form.get('action2') == 'send_email':

#             subject = request.form.get('subject')
#             body = request.form.get('body')
#             smtp_server = "smtp.gmail.com"

#             with sqlite3.connect('database.sqlite') as conn:
#                 send_email(subject, body, smtp_server, conn)
            
#     return render_template('send.html')
