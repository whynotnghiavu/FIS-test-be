# from fastapi.security import OAuth2PasswordRequestForm
# from fastapi import APIRouter, Depends, Response, status
# from sqlalchemy.orm import Session
# from ..database.get_db import get_db
# from typing import Annotated


# from ..schemas import user as _schemas_user
# from ..services import user as _services_user

# from ..services.get_user_id import GetUserId


# from ..models import Role
# from ..services.role_checker import RoleChecker
# from ..services.auth import validate_otp


# router = APIRouter(prefix="/users")




 



# @router.post('/register')
# def register(
#     user: _schemas_user.UserRegister,
#     _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
#     _otp: Annotated[bool, Depends(validate_otp)],
#     db: Session = Depends(get_db)
# ):
#     return _services_user.register(user, db)


# @router.post('/login')
# def login(
#     form_data: Annotated[OAuth2PasswordRequestForm, Depends()],
#     db: Session = Depends(get_db)
# ):
#     user = _schemas_user.UserLogin(
#         email=form_data.username,
#         password=form_data.password,
#     )
#     return _services_user.login(user, db)


# @router.get("/current-user-id")
# def current_user_id(
#     user_id: Annotated[str, Depends(GetUserId())],
# ):
#     return {"user_id": user_id}


# @router.get("/demo-frontend-qr")
# def demo_frontend_qr(
#     user_id: Annotated[str, Depends(GetUserId())],
#     db: Session = Depends(get_db)
# ):
#     return _services_user.demo_frontend_qr(user_id, db)


# @router.post("/verify-otp")
# def verify_otp(
#     otp: str,
#     user_id: Annotated[str, Depends(GetUserId())],
#     db: Session = Depends(get_db)
# ):
#     return _services_user.verify_otp(otp, user_id, db)


# @router.get("/save-recovery-otp")
# def save_recovery_otp(
#     user_id: Annotated[str, Depends(GetUserId())],
#     _otp: Annotated[bool, Depends(validate_otp)],
#     db: Session = Depends(get_db)
# ):
#     return _services_user.save_recovery_otp(user_id, db)


# @router.post("/verify-recovery-otp")
# def verify_recovery_otp(
#     code: str,
#     user_id: Annotated[str, Depends(GetUserId())],
#     db: Session = Depends(get_db)
# ):
#     return _services_user.verify_recovery_otp(code, user_id, db)
