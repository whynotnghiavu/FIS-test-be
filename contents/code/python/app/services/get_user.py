from typing import Annotated
from fastapi import Depends, HTTPException, status
from ..schemas.user import JWTUser
from .auth import validate_token


class GetUser:
    def __init__(self):
        pass

    def __call__(self, user: Annotated[JWTUser, Depends(validate_token)]):
        return user.get('email')
