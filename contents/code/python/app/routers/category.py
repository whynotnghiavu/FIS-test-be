from fastapi import APIRouter, Depends,  status
from sqlalchemy.orm import Session
from ..database.get_db import get_db

from typing import List, Annotated


from ..schemas import category as _schemas_category
from ..services import category as _services_category


from ..models import Role
from ..services.role_checker import RoleChecker
from ..services.auth import validate_otp


router = APIRouter(prefix="/categories")


@router.post("", response_model=_schemas_category.Category, status_code=status.HTTP_201_CREATED)
def create_category(
    category: _schemas_category.CategoryCreate,
    _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
    _otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):
    return _services_category.create(category, db)


@router.get("", response_model=List[_schemas_category.Category])
def get_all_categories(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return _services_category.get_all(db, skip, limit)


@router.get("/{category_id}", response_model=_schemas_category.Category)
def get_one_category_by_id(category_id: int, db: Session = Depends(get_db)):
    return _services_category.get_by_id(category_id, db)


@router.put("/{category_id}", response_model=_schemas_category.Category)
def update_category(
    category_id: int,
    category: _schemas_category.CategoryUpdate,
    _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
    _otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):
    return _services_category.update(category_id, category, db)


@router.delete("/{category_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_category(
    category_id: int,
    _: Annotated[bool, Depends(RoleChecker(allowed_roles=[Role.ADMIN]))],
    _otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):
    return _services_category.remove(category_id, db)
