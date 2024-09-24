import os
from datetime import datetime, timedelta, timezone

JWT_EXPIRE_SECONDS = int(os.getenv("OTP_EXPIRE_SECONDS", 60 * 60 * 24 * 2))

jwt_expire = datetime.now() + timedelta(seconds=JWT_EXPIRE_SECONDS)
print("🐍 File: python/a.py | Line: 2 | undefined ~ jwt_expire", jwt_expire)

# datetime.now(timezone.utc)
jwt_expire = int(jwt_expire.timestamp())
print("🐍 File: python/a.py | Line: 2 | undefined ~ jwt_expire", jwt_expire)
