from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from db import get_db
from models import User
from repository.user_repository import UserRepository
from schemas.user_schemas import User_schemas
from schemas.token_schemas import Token, TokenData, LoginRequest
from schemas.jwt_handler import create_tokens,verify_token

router = APIRouter()


@router.post("/signup")
def signup(user: User_schemas, db: Session = Depends(get_db)):
    user_repository = UserRepository(db)
    # Convert Pydantic schema to SQLAlchemy model
    existing_user = user_repository.get_user_by_email(user.email)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    db_user = User(email=user.email, password=user.password)
    user_repository.add_user(db_user)
    return {"message": "User signed up successfully"}


@router.post("/login", response_model=Token)
def login(credentials: LoginRequest, db: Session = Depends(get_db)):
    """Authenticate user and return access and refresh tokens."""
    user_repository = UserRepository(db)
    user = user_repository.get_user_by_email(credentials.email)
    
    if not user or user.password != credentials.password:
        raise HTTPException(
            status_code=401,
            detail="Invalid email or password",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    return create_tokens(user.id, user.email)


@router.post("/refresh", response_model=Token)
def refresh_token(token_data: TokenData, db: Session = Depends(get_db)):
    """Get new access and refresh tokens using a valid refresh token."""
    payload = verify_token(token_data.refresh_token, token_type="refresh")  
    
    if not payload:
        raise HTTPException(
            status_code=401,
            detail="Invalid or expired refresh token",
            headers={"WWW-Authenticate": "Bearer"}
        )
    
    user_repo = UserRepository(db)
    user = user_repo.get_user_by_email(payload.get("email"))
    
    if not user:
        raise HTTPException(status_code=401, detail="User not found")
    
    return create_tokens(user.id, user.email)