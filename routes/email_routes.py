from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from db import get_db
from utils.email_sender import send_email
from schemas.email_schemas import EmailRequest

router = APIRouter()

@router.post("/send-email")
def send_email_route(email:str,subject:str,content:str):
    
        send_email(email, subject, content)
        return {"message": "Email sent successfully"}
