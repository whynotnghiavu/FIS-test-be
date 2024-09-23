import qrcode
import time
import pyotp

# API: Đăng nhập, Đăng ký
# Tạo mã bí mật và lưu SQL
secret = pyotp.random_base32()
print("🐍 File: python/a.py | Line: 6 | undefined ~ secret", secret)
# Trả ra JWT có isEnableOTP=False


# API: Scan QR Code OTP


totp = pyotp.TOTP(secret)
otp_url = totp.provisioning_uri(
    issuer_name="Test Kĩ Năng Backend",
    name="user@example.com"
)
qr = qrcode.make(otp_url)
# qr.save("otp_qr_code.png")
qr.show()