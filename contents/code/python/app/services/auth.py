import os
import jwt
from fastapi.security import HTTPBearer
from fastapi import Depends, HTTPException
from datetime import datetime, timedelta
from pydantic import ValidationError
from ..schemas import user as _schemas_user




JWT_SECURITY_ALGORITHM = os.getenv("JWT_SECURITY_ALGORITHM", "HS256")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "SECRET_KEY")
JWT_EXPIRE_SECONDS = int(os.getenv("JWT_EXPIRE_SECONDS", 60*60*24*3))





reusable_oauth2 = HTTPBearer(
    scheme_name='Authorization'
)


def generate_token(user: _schemas_user.User):
    expire = datetime.now() + timedelta(seconds=JWT_EXPIRE_SECONDS)

    to_encode = {
        "exp": expire,
        "email": user.email,
        "role": user.role
    }

    encoded_jwt = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_SECURITY_ALGORITHM)

    return {"token": encoded_jwt}


def validate_token(token=Depends(reusable_oauth2)) -> str:
    try:
        payload = jwt.decode(token.credentials, JWT_SECRET_KEY, algorithms=[JWT_SECURITY_ALGORITHM])

        exp_time = datetime.fromtimestamp(payload.get('exp'))
        if exp_time < datetime.now():
            raise HTTPException(status_code=403, detail="Token expired")

        return {
            "email": payload.get('email'),
            "role": payload.get('role'),
        }

    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(status_code=403, detail="Could not validate credentials")
