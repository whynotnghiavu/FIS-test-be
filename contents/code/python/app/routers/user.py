from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.get_db import get_db

from typing import Annotated

from ..schemas import user as _schemas_user

from ..services import user as _services_user
from ..services.get_user_id import GetUserId
from ..services.auth import validate_otp


from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO


from ..services.role_checker import RoleChecker
from ..models import Role


router = APIRouter(prefix="/users")


@router.post('/login')
def login(
    user: _schemas_user.UserLogin,
    db: Session = Depends(get_db)
):
    return _services_user.login(user, db)


@router.get("/generate-qr")
def generate_qr(
    user_id: Annotated[str, Depends(GetUserId())],
    db: Session = Depends(get_db)
):
    otp_url = _services_user.generate_qr(user_id, db)

    qr_img = qrcode.make(otp_url)
    img_io = BytesIO()
    qr_img.save(img_io, 'PNG')
    img_io.seek(0)

    return StreamingResponse(img_io, media_type="image/png")


@router.post("/verify-otp")
def verify_otp(
    otp: str,
    user_id: Annotated[str, Depends(GetUserId())],
    db: Session = Depends(get_db)
):
    return _services_user.verify_otp(otp, user_id, db)


@router.post('/register')
def register(
    user: _schemas_user.UserRegister,
    _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
    otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):
    return _services_user.register(user, db)
