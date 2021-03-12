from fastapi import status
from fastapi.security import OAuth2PasswordRequestForm
from fastapi import APIRouter,Depends,HTTPException

from core.token_generator import TokenGenerator
from db.models.users import Users
from db.repositories.auth import authenticate_user

auth_router = APIRouter(tags=["Authentication"])


@auth_router.post("/login/")
def login(request: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(database.get_db)):
    user = db.query(Users).filter(models.User.email == request.username).first()
    exception = HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Invalid Credentials")
    if not user:
        raise exception
    if not Hash.verify(user.password, request.password):
        raise exception

    access_token = TokenGenerator().create_access_token(data={"sub": user.email})
    return {"access_token": access_token, "token_type": "bearer"}

