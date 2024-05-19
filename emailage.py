from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart   
import smtplib, ssl
from database import fetch_all_contact_emails

sender_email = 'emailtester.automate@gmail.com'
password = 'fryplilvvsijpilv'

def send_email(subject, body, smtp_server, conn):
        contacts = fetch_all_contact_emails(conn)
        msg = MIMEMultipart()
        msg["From"] = sender_email
        msg["Subject"] = subject
        msg.attach(MIMEText(body, "plain"))
        message_string = msg.as_string()
        ontext = ssl.create_default_context()

        for contacts in contacts: 
            server = smtplib.SMTP_SSL(smtp_server, 465)
            server.login(sender_email, password)
            server.sendmail(sender_email, contacts, message_string)
