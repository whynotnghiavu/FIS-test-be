from fastapi.responses import JSONResponse
import pyotp
from fastapi import HTTPException, status, Response
from fastapi.responses import StreamingResponse
from sqlalchemy.orm import Session

from ..schemas import user as _schemas_user


from .. import models


from . import auth


import qrcode
import base64
from io import BytesIO


from . import cryptography
from ..logger import logger


def create_superuser(user: _schemas_user.UserRegister, db: Session):
    count_user = db.query(models.User).count()

    if count_user == 0:
        user.password = cryptography.hash_password(user.password)
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)


def login(user: _schemas_user.UserLogin, db: Session):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login information",
            headers={"WWW-Authenticate": "Bearer"},
        )

    if not cryptography.verify_password(user.password, db_user.password):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect login information",
            headers={"WWW-Authenticate": "Bearer"},
        )

    jwt_token = auth.generate_token(db_user, time_otp_expire=0)

    if not db_user.is_enable_otp:
        otp_qr_code = generate_qr(db_user.id, db)
        return {
            "otp_qr_code": otp_qr_code,
            "access_token": jwt_token.get('access_token'),
            "token_type": jwt_token.get('token_type'),
        }
    return jwt_token


def generate_qr(user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found"
        )

    if not db_user.otp_secret:
        otp_secret = pyotp.random_base32()
        print("🐍 File: services/user.py | Line: 73 | generate_qr ~ otp_secret", otp_secret)
        otp_secret = cryptography.encrypt(otp_secret)
        print("🐍 File: services/user.py | Line: 75 | generate_qr ~ otp_secret", otp_secret)
        db_user.otp_secret = otp_secret

    totp = pyotp.TOTP(db_user.otp_secret)
    provisioning_uri = totp.provisioning_uri(
        issuer_name="Test Kĩ Năng Backend",
        name=str(user_id)
    )
    print("🐍 File: services/user.py | Line: 84 | generate_qr ~ provisioning_uri",provisioning_uri)

    qr_img = qrcode.make(provisioning_uri)
    buffered = BytesIO()
    qr_img.save(buffered, "PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')
    db_user.otp_qr_code = qr_base64
    db.commit()
    db.refresh(db_user)

    return qr_base64


def demo_frontend_qr(user_id: int, db: Session):
    qr_base64 = generate_qr(user_id, db)

    img_data = base64.b64decode(qr_base64)
    buffered = BytesIO(img_data)

    return StreamingResponse(buffered, media_type="image/png")


def verify_otp(otp: int, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found"
        )

    if not db_user.otp_secret:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"User has not scanned otp"
        )

    otp_secret = db_user.otp_secret
    print("🐍 File: services/user.py | Line: 119 | verify_otp ~ otp_secret", otp_secret)
    otp_secret = cryptography.decrypt(otp_secret)
    print("🐍 File: services/user.py | Line: 121 | verify_otp ~ otp_secret", otp_secret)
    totp = pyotp.TOTP(otp_secret)
    print("🐍 File: services/user.py | Line: 105 | undefined ~ otp", otp)
    print("🐍 File: services/user.py | Line: 124 | verify_otp ~ totp.now()", totp.now())

    if not totp.verify(otp):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"OTP code is incorrect"
        )

    db_user.is_enable_otp = True
    db.commit()
    db.refresh(db_user)

    return auth.generate_token(db_user)


def register(user: _schemas_user.UserRegister, db: Session):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail=f"Email '{user.email}' already exists.")

    user.password = cryptography.hash_password(user.password)
    new_user = models.User(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return auth.generate_token(new_user, time_otp_expire=0)
# Tạo OTP như đăng nhập
