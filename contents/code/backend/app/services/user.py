import pyotp
from fastapi import HTTPException, status
from fastapi.responses import StreamingResponse

from sqlalchemy.orm import Session
from .. import models
from ..schemas import user as _schemas_user
from . import cryptography


from . import auth
from .generate_random_string import generate_random_string


import qrcode
import base64
from io import BytesIO


from ..logger import setup_logger
logger = setup_logger(__name__)


def create_superuser(user: _schemas_user.UserRegister, db: Session):
    if user.password != user.password_confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )

    count_user = db.query(models.User).count()

    if count_user == 0:
        user.password = cryptography.hash_password(user.password)
        new_user = models.User(
            email=user.email,
            password=user.password,
            role=user.role,
        )
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

    if not db_user.is_enable_otp:
        otp_qr_code = generate_qr(db_user.id, db)
        jwt_token = auth.generate_token(db_user, time_otp_expire=0)
        return {
            "otp_qr_code": otp_qr_code,
            "access_token": jwt_token.get('access_token'),
        }

    jwt_token = auth.generate_token(db_user)
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
        logger.debug(otp_secret)
        db_user.otp_secret = cryptography.encrypt(otp_secret)
        logger.debug(otp_secret)

    otp_secret = db_user.otp_secret
    logger.debug(otp_secret)
    otp_secret = cryptography.decrypt(otp_secret)
    logger.debug(otp_secret)

    totp = pyotp.TOTP(otp_secret)
    provisioning_uri = totp.provisioning_uri(
        issuer_name="Test Kĩ Năng Backend",
        name=str(user_id)
    )
    logger.debug(provisioning_uri)

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
    logger.debug(otp_secret)
    otp_secret = cryptography.decrypt(otp_secret)
    logger.debug(otp_secret)

    totp = pyotp.TOTP(otp_secret)
    logger.debug(otp)
    logger.debug(totp.now())

    if not totp.verify(otp):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"OTP code is incorrect"
        )

    db_user.is_enable_otp = True
    db.commit()
    db.refresh(db_user)

    return auth.generate_token(db_user)


def save_recovery_otp(user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found"
        )

    otp_list = []
    for _ in range(6):
        otp_list.append(generate_random_string())

    db_user.otp_recovery = otp_list
    db.commit()
    db.refresh(db_user)

    return otp_list


def verify_recovery_otp(code: str, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User not found"
        )

    if code not in db_user.otp_recovery:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Code OTP recovery is incorrect"
        )

    db_user.otp_secret = False
    db_user.is_enable_otp = False
    db.commit()
    db.refresh(db_user)

    otp_qr_code = generate_qr(db_user.id, db)
    return {
        "otp_qr_code": otp_qr_code,


    }


def register(user: _schemas_user.UserRegister, db: Session):
    if user.password != user.password_confirm:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Passwords do not match"
        )

    db_user = db.query(models.User).filter(models.User.email == user.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Email '{user.email}' already exists."
        )

    user.password = cryptography.hash_password(user.password)
    new_user = models.User(
        email=user.email,
        password=user.password,
        role=user.role,
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return auth.generate_token(new_user, time_otp_expire=0)
