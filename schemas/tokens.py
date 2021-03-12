from typing import Optional

from schemas.base_class import CoreModel


class Token(CoreModel):
    access_token: str
    token_type: str


class TokenData(CoreModel):
    username: Optional[str] = None
