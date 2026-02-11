import smtplib
from email.message import EmailMessage
from dotenv import load_dotenv
import os
load_dotenv()
password=os.getenv("PASSWORD")
sender_email=os.getenv("SENDER_EMAIL")
#email details
def send_email(reciever_email:str, subject:str, content:str)->str:
    """Send an email to the specified recipient"""
    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = reciever_email
    msg["Subject"] = subject
    msg.set_content(content)

    # Send email
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        #server.starttls()
        server.login(sender_email, password)
        server.send_message(msg)

    return("Email sent successfully!")