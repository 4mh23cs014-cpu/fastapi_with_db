from datetime import datetime,timedelts
from typing import Optional
from jose import JWTError,jwt
import os

SECRET_KEY = os.getenv("JWT_SECRET_KEY","Your-super-secret-key-change-in-prod")
ALGORITHM = "HS256" 
ACCESS_TOKEN_EXPIRE_MINUTES = 30
REFRESH_TOKEN_EXPIRE_DAYS = 7

def create_access_token(data:dict,expires_delta:Optional[timedelta ]=None):
    to_encode = data.copy()
    expires = datetime.utcnow() + (expires_delta or timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES))
    to_encode.update({"exp": expires,"type":"access"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  

def create_refresh_token(data:dict,expires_delta:Optional[timedelta ]=None):
    to_encode = data.copy()
    expires = datetime.utcnow() + (expires_delta or timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS))
    to_encode.update({"exp": expires,"type":"refresh"})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)  
def verify_token(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except JWTError:
        return None 
def create_token(user_id: int, user_email: str)->dict:
    token_data = {"user_id": user_id, "email":email}
    return {"access_token": create_access_token(token_data),
            "refresh_token": create_refresh_token(token_data),
            "token_type": "bearer"  }
