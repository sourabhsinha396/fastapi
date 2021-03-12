from typing import Optional
from sqlalchemy.orm import Session

from db.models.users import Users
from schemas.users import UserInDB
from core.security import Hasher


def authenticate_user(email: str,password: str,db: Session) -> Optional[UserInDB]:
    user_by_email = db.query(Users).filter(Users.email==email)
    user_by_username = db.query(Users).filter(Users.username == email)
    user = user_by_username or user_by_email
    print("here us",user)
    if not (user):
        return None
    if not Hasher().verify(password,user.first().password):
        return None
    return user.first()