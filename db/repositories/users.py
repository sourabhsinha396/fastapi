from sqlalchemy.orm import Session
from fastapi import HTTPException, status
from core.security import Hasher

from db.models.users import Users
from schemas.users import UserCreate


def verify_unique_user(request,db):
    verified_email = get_user_by_email(request.email,db)
    verified_username = get_user_by_username(request.username,db)
    if verified_email and verified_username:
        print("1hy")
        return True
    raise HTTPException(status_code=status.HTTP_406_NOT_ACCEPTABLE,detail="We already have an user with same username/email")


def get_user_by_email(email,db):
    user = db.query(Users).filter(Users.email == email)
    if not user.first():
        return True #user does not exist,good thing
    return False


def get_user_by_username(username,db):
    user = db.query(Users).filter(Users.username == username)
    if not user.first():
        return True
    return False


def create(request: UserCreate, db: Session):
    new_user = Users(username=request.username,email=request.email, password=Hasher.hash(request.password))
    verify_unique_user(request,db)
    db.add(new_user)
    try:
        db.commit()
    except Exception as e:
        print(e)
    db.refresh(new_user)
    return new_user

