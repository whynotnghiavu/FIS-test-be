from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import user as _schemas_user




from ..models.category import Category as _models_category
from ..models.post import Post as _models_post
from ..models.comment import Comment as _model_comment
from ..models.user import User as _model_user






from . import auth
from . import manager_password


def register(user: _schemas_user.UserRegister, db: Session):
    db_user = db.query(_model_user).filter(_model_user.email == user.email).first()
    if db_user:
        raise HTTPException(status_code=400, detail=f"Email '{user.email}' already exists.")

    user.password = manager_password.hash_password(user.password)
    new_user = _model_user(**user.model_dump())
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return auth.generate_token(new_user)


def login(user: _schemas_user.UserRegister, db: Session):
    db_user = db.query(_model_user).filter(_model_user.email == user.email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Incorrect login information")

    if not manager_password.verify_password(user.password, db_user.password):
        raise HTTPException(status_code=400, detail=f"Incorrect login information")

    return auth.generate_token(db_user)
