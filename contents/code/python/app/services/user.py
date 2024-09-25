import pyotp
from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..schemas import user as _schemas_user


from .. import models


from . import auth


import qrcode
import base64
from io import BytesIO


from . import cryptography


def create_superuser(user: _schemas_user.UserRegister, db: Session):
    count_user = db.query(models.User).count()

    if count_user == 0:
        user.password = cryptography.hash_password(user.password)
        new_user = models.User(**user.model_dump())
        db.add(new_user)
        db.commit()
        db.refresh(new_user)


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


def login(user: _schemas_user.UserLogin, db: Session):
    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Incorrect login information")

    if not cryptography.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail=f"Incorrect login information")

    return auth.generate_token(db_user, time_otp_expire=0)


def generate_qr(user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found"
        )

    if not db_user.otp_secret:
        otp_secret = pyotp.random_base32()
        otp_secret = cryptography.encrypt(otp_secret)
        db_user.otp_secret = otp_secret

    totp = pyotp.TOTP(db_user.otp_secret)
    provisioning_uri = totp.provisioning_uri(
        issuer_name="Test Kĩ Năng Backend",
        name=str(user_id)
    )

    qr_img = qrcode.make(provisioning_uri)

    buffered = BytesIO()
    qr_img.save(buffered, "PNG")
    qr_base64 = base64.b64encode(buffered.getvalue()).decode('utf-8')

    db_user.otp_qr_code = qr_base64

    db.commit()
    db.refresh(db_user)

    return qr_base64


def verify_otp(otp: int, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    if not db_user.otp_secret:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"User has not scanned otp")

    otp_secret = db_user.otp_secret

    totp = pyotp.TOTP(otp_secret)

    if not totp.verify(otp):
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"OTP code is incorrect")

    return auth.generate_token(db_user)
