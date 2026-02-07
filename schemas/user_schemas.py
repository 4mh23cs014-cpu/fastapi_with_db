from pydantic import BaseModel      

class User_schemas(BaseModel):
     name: str
     email: str
