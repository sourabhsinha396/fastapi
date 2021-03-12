
from fastapi import APIRouter
from fastapi import Depends
from fastapi import status
from sqlalchemy.orm import Session

from db.session import get_db
from schemas.users import UserCreate,ShowUser,UserPublic
from db.repositories.users import create

from schemas.tokens import AccessToken
from core.token_generator import TokenGenerator

user_router = APIRouter()


@user_router.post("/create/user/")
def create_new_user(request_body: UserCreate,db: Session = Depends(get_db)):
    created = create(request_body,db)
    access_token = AccessToken(
        access_token=TokenGenerator().create_access_token_for_user(user=created), token_type="bearer"
    )
    return access_token

