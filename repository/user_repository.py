from model import user
from sqlalchemy.orm import Session
class user_repository:
    def __init__(self,db:Session):
        self.db=db
    def add_user(self, user: user):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user