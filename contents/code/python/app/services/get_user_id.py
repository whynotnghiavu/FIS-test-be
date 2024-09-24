from typing import Annotated
from fastapi import Depends, HTTPException, status
from .auth import validate_token

from ..schemas.user import JWTUser


class GetUserId:
    def __init__(self):
        pass

    def __call__(self, user: Annotated[JWTUser, Depends(validate_token)]):
        if user.get('user_id'):
            return user.get('user_id')

        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="You do not have access to this resource"
        )
