from fastapi import APIRouter,HTTPException 
from sqlalchemy.orm import Session
from fastapi import Depends
from db import get_db
from models import User
from repository.user_repository import UserRepository
from schemas.user_schemas import User_schemas
router = APIRouter()


@router.post("/signup")
def signup(user: User_schemas, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    # Convert Pydantic schema to SQLAlchemy model
    exitsting_user = user_repository.get_user_by_email(user.email)
    if exitsting_user:
        raiseHTTPException(status_code=400, detail="User already exists")   
    
    db_user = User(email=user.email, password=user.password)
    user_repository.add_user(db_user)
    return {"message": "User signed up successfully"}

@router.post("/login")
def login():
    return {"message": "User logged in successfully"}