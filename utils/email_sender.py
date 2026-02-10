import smtplib
from email.message import EmailMessage
import os
from dotenv import load_dotenv

def send_email(to_email: str, subject: str, body: str) -> str:
    """
    Sends an email to the specified recipient.
    """
    load_dotenv()
    sender_email = os.getenv("SENDER_EMAIL")
    app_password = os.getenv("APP_PASSWORD")

    if not sender_email or not app_password:
        raise ValueError("SENDER_EMAIL and APP_PASSWORD must be set in .env file")

    msg = EmailMessage()
    msg["From"] = sender_email
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.set_content(body)

    try:
        with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
            server.login(sender_email, app_password)
            server.send_message(msg)
        return "Email sent successfully"
    except Exception as e:
        print(f"Failed to send email: {e}")
        raise e