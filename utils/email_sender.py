import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv
load_dotenv()
   
sender_email = os.getenv("SENDER_EMAIL")
app_password = os.getenv("APP_PASSWORD")

def send_email(to_email: str, subject: str, content: str) -> str:

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(content )

   
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(sender_email, app_password)
        server.send_message(msg)
            
print("Email sent successfully")
