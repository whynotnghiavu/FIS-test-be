from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.get_db import get_db

from typing import Annotated

from ..schemas import user as _schemas_user

from ..services import user as _services_user
from ..services.get_user_id import GetUserId


from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO


from ..models import Role
from ..services.role_checker import RoleChecker
from ..services.auth import validate_otp


router = APIRouter(prefix="/users")


@router.post('/register')
def register(
    user: _schemas_user.UserRegister,
    _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
    _otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):

    return _services_user.register(user, db)


@router.post('/login')
def login(
    user: _schemas_user.UserLogin,
    db: Session = Depends(get_db)
):
    return _services_user.login(user, db)


@router.get("/generate-qr-base64")
def generate_qr_base64(
    user_id: Annotated[str, Depends(GetUserId())],
    db: Session = Depends(get_db)
):
    return _services_user.generate_qr(user_id, db)

# @router.get("/generate-qr")
# @router.get("/generate-qr")
# @router.get("/generate-qr")


@router.get("/generate-qr-image")
def generate_qr_image(
    user_id: Annotated[str, Depends(GetUserId())],
    db: Session = Depends(get_db)
):
    import base64
    qr_base64 = _services_user.generate_qr(user_id, db)

    img_data = base64.b64decode(qr_base64)
    img_io = BytesIO(img_data)
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")


@router.post("/verify-otp")
def verify_otp(
    otp: str,
    user_id: Annotated[str, Depends(GetUserId())],
    db: Session = Depends(get_db)
):
    return _services_user.verify_otp(otp, user_id, db)
