import os
from ..database.get_db import get_db

from ..models import Role
from ..schemas import user as _schemas_user
from ..services import user as _services_user


from ..logger import logger


def create_superuser():
    user = _schemas_user.UserRegister(
        email=os.getenv("EMAIL_ADMIN_DEFAULT", "admin@gmail.com"),
        password=os.getenv("PASSWORD_ADMIN_DEFAULT", "admin@A8"),
        role=Role.ADMIN
    )
    
    print("🐍 File: seeders/create_superuser.py | Line: 18 | create_superuser ~ user",user)

    return _services_user.create_superuser(user, next(get_db()))
