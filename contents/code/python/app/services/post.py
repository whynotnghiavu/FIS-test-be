from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import post as _schemas_post


from ..models.category import Category as _models_category
from ..models.post import Post as _models_post
from ..models.comment import Comment as _model_comment
from ..models.user import User as _model_user


def create(post: _schemas_post.PostCreate, db: Session):
    db_category = db.query(_models_category).filter(_models_category.id == post.category_id).first()
    if not db_category:
        raise HTTPException(status_code=400, detail=f"Category not found")

    new_post = _models_post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(_models_post).offset(skip).limit(limit).all()


def get_by_id(post_id: int, db: Session):
    return db.query(_models_post).filter(_models_post.id == post_id).first()


def update(post_id: int, post: _schemas_post.PostUpdate, db: Session):
    if post.category_id != None:
        db_category = db.query(_models_category).filter(_models_category.id == post.category_id).first()
        if not db_category:
            raise HTTPException(status_code=400, detail=f"Category not found")

    db_post = db.query(_models_post).filter(_models_post.id == post_id).first()
    if db_post is None:
        return None

    for key, value in post.model_dump(exclude_unset=True).items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


def remove(post_id: int, email: str, db: Session):
    db_user = db.query(_model_user).filter(_model_user.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Email không tồn tại")

    db_post = db.query(_models_post).filter(_models_post.id == post_id).first()
    if db_post is None:
        return None

    if db_user.id != db_post.user_id:
        raise HTTPException(status_code=400, detail=f"Người dùng không phải chủ của bài đăng")

    db.delete(db_post)
    db.commit()
    return db_post
