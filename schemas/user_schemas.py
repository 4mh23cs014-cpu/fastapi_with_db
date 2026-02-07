from pydantic import BaseModel      

class User_schemas(BaseModel):
     password: str
     email: str
