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
