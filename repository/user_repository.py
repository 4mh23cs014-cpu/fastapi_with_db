from models import User
from sqlalchemy.orm import Session


class UserRepository:
    def __init__(self, db: Session):
        self.db = db

    def add_user(self, user: User):
        self.db.add(user)
        self.db.commit()
        self.db.refresh(user)
        return user

    def get_user_by_email(self, email: str):
        return self.db.query(User).filter(User.email == email).first()  