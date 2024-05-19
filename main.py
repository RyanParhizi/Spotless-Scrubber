from flask import Flask, render_template, request
import sqlite3
from database import add_contact, fetch_all_contacts, remove_contacts_by_ID
from emailage import send_email


app = Flask(__name__) 

@app.route("/")
def home():
    return render_template("home.html")

@app.route("/send")
def send():
    return render_template("send.html")

@app.route("/database")
def database():

    # if request.method == 'POST':
    #     if request.form.get('action') == 'send_email':

    with sqlite3.connect('database.sqlite') as conn:
        contacts = fetch_all_contacts(conn)

    return render_template("database.html", contacts = contacts)
 
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

# app.route('/database', methods=['GET', 'POST'])
# def database():
#     if request.method == 'POST':

#         if request.form.get('action1') == 'add_contact':
        
#             firstname = request.form.get('firstname')
#             lastname = request.form.get('lastname')
#             phone = request.form.get('phone')
#             email = request.form.get('email')
        
#             with sqlite3.connect('database.sqlite') as conn:
#                 add_contact(firstname, lastname, phone, email, conn)

#         elif request.form.get('action3') == 'remove_contact':
#             ID_num = request.form.get('ID number')

#             with sqlite3.connect('database.sqlite') as conn:
#                     remove_contacts_by_ID(ID_num, conn)

#     with sqlite3.connect('database.sqlite') as conn:
#         contacts = fetch_all_contacts(conn)

#     return render_template('database.html', contacts=contacts)

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=3000)
