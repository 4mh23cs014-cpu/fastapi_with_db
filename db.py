from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv
import os

load_dotenv()   

Base=declarative_base()


DATABASE_URL = os.getenv("DATABASE_URL")
if DATABASE_URL:
    DATABASE_URL = DATABASE_URL.replace("postgres://", "postgresql://")
print("DAT  ABASE_URL",DATABASE_URL)

if DATABASE_URL and DATABASE_URL.startswith("sqlite"):
    engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
else:
    engine = create_engine(DATABASE_URL, connect_args={"sslmode": "require"})
sessionlocal=sessionmaker(autocommit=False,autoflush=False,bind=engine) 

def get_db():
    db =    sessionlocal()    
    try:
        yield db
    finally:
        db.close()  