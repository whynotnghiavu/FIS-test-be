import os
import jwt

from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException, status
from datetime import datetime, timedelta
from pydantic import ValidationError


from ..schemas import user as _schemas_user


JWT_SECURITY_ALGORITHM = os.getenv("JWT_SECURITY_ALGORITHM", "HS256")
JWT_SECRET_KEY = os.getenv("JWT_SECRET_KEY", "SECRET_KEY")
JWT_EXPIRE_SECONDS = int(os.getenv("JWT_EXPIRE_SECONDS", 60 * 60 * 24 * 3))
# OTP_EXPIRE_SECONDS = int(os.getenv("OTP_EXPIRE_SECONDS", 60 * 60 * 24 * 2))
# OTP_EXPIRE_SECONDS = int(os.getenv("OTP_EXPIRE_SECONDS", 60 ))
OTP_EXPIRE_SECONDS = 60


oauth2_scheme = OAuth2PasswordBearer(tokenUrl="api/v1/users/login")


def generate_token(user: _schemas_user.User, time_otp_expire=OTP_EXPIRE_SECONDS):
    jwt_expire = datetime.now() + timedelta(seconds=JWT_EXPIRE_SECONDS)
    otp_expire = datetime.now() + timedelta(seconds=time_otp_expire)

    to_encode = {
        "user_id": user.id,
        "role": user.role,
        "jwt_expire": int(jwt_expire.timestamp()),
        "otp_expire": int(otp_expire.timestamp()),
    }

    token = jwt.encode(to_encode, JWT_SECRET_KEY, algorithm=JWT_SECURITY_ALGORITHM)

    return {
        "access_token": token,
    }


def validate_token(token=Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_SECURITY_ALGORITHM])

        jwt_expire = datetime.fromtimestamp(payload.get('jwt_expire'))
        if jwt_expire < datetime.now():
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Token expired")

        return {
            "user_id": payload.get('user_id'),
            "role": payload.get('role'),
        }

    except:
        raise HTTPException(
            status_code=status.HTTP_403_FORBIDDEN,
            detail="Could not validate credentials"
        )


def validate_otp(token=Depends(oauth2_scheme)) -> str:
    try:
        payload = jwt.decode(token, JWT_SECRET_KEY, algorithms=[JWT_SECURITY_ALGORITHM])

        otp_expire = datetime.fromtimestamp(payload.get('otp_expire'))
        if otp_expire < datetime.now():
            raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="OTP expired")

        return {
            "user_id": payload.get('user_id'),
            "role": payload.get('role'),
        }

    except (jwt.PyJWTError, ValidationError):
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN, detail="Could not validate credentials")
