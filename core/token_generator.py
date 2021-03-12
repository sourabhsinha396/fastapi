import jwt 
from datetime import datetime,timedelta
from core.config import SECRET_KEY, ALGORITHM,ACCESS_TOKEN_EXPIRE_MINUTES
from schemas.users import UserPasswordUpdate, UserInDB


class TokenGenerator:
    def create_access_token(email):
        to_encode = data.copy()
        if expires_delta:
            expire = datetime.utcnow() + expires_delta
        else:
            expire = datetime.utcnow() + timedelta(minutes=15)
        to_encode.update({"exp": expire})
        encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
        return encoded_jwt
