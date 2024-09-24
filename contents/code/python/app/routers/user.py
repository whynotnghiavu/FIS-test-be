from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..database.get_db import get_db

from typing import Annotated

from ..schemas import user as _schemas_user

from ..services import user as _services_user
from ..services.get_user_id import GetUserId

# from ..services.role_checker import RoleChecker
# from ..models import Role

from fastapi.responses import StreamingResponse
import qrcode
from io import BytesIO



router = APIRouter(prefix="/users")


# @router.post('/register')
# def register(
#     user: _schemas_user.UserRegister,
#     _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
#     db: Session = Depends(get_db)
# ):
#     return _services_user.register(user, db)


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
 
 
# @router.post("/verify_OTP")
# def verify_OTP():
#     return True

# # # API: Verify   OTP
# # totp.verify('492039')  # => True
