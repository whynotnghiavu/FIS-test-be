from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session


from ..database.get_db import get_db


from ..schemas import user as _schemas_user
from ..services import user as _services_user

from ..services.role_checker import RoleChecker
from ..models import Role
from typing import Annotated

router = APIRouter(prefix="/user")


@router.post('/register')
def register(
    user: _schemas_user.UserRegister,
    _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
    db: Session = Depends(get_db)
):
    return _services_user.register(user, db)


@router.post('/login')
def login(user: _schemas_user.UserLogin, db: Session = Depends(get_db)):
    return _services_user.login(user, db)


# Gắn JWT sau

# Gắn SQL sau
# tìm cách hiển thị QR


@router.get("/generate-qr")
def generate_qr():
    # Create a TOTP object
    import pyotp
    import qrcode
    from io import BytesIO
    from fastapi.responses import StreamingResponse

    totp = pyotp.TOTP("SECRET")
    
    # Generate the provisioning URI
    otp_url = totp.provisioning_uri(
        issuer_name="Test Kĩ Năng Backend",
        name="user@example.com"
    )
    
    # Generate a QR code for the provisioning URI
    qr_img = qrcode.make(otp_url)
    
    # Create an in-memory buffer to hold the image
    img_io = BytesIO()
    qr_img.save(img_io, 'PNG')
    img_io.seek(0)
    
    # Return the QR code as an image
    return StreamingResponse(img_io, media_type="image/png")
@router.get("/scan_QR_code_OTP")
def scan_QR_code_OTP():

# # API: Đăng nhập, Đăng ký
# # Tạo mã bí mật và lưu SQL
# secret = pyotp.random_base32()
# print("🐍 File: python/a.py | Line: 6 | undefined ~ secret", secret)
# # Trả ra JWT có isEnableOTP=False


# # API: Scan QR Code OTP
# Truy vấn SQL lấy Mã bí mật
    secret = 'nghia'


    import pyotp
    totp = pyotp.TOTP(secret)
    otp_url = totp.provisioning_uri(
        issuer_name="Test Kĩ Năng Backend",
        name="user@example.com"
    )


# qr = qrcode.make(otp_url)
# # qr.save("otp_qr_code.png")
# qr.show()
    pass

@router.post("/verify_OTP")
def verify_OTP():
    return True

# # API: Verify   OTP
# totp.verify('492039')  # => True

