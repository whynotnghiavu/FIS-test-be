from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import post as _schemas_post

from .. import models
 


def create(post: _schemas_post.PostCreate, email: str, db: Session):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Email user not found")

    db_category = db.query(models.Category).filter(models.Category.id == post.category_id).first()
    if not db_category:
        raise HTTPException(status_code=400, detail=f"Category not found")

    new_post = models.Post(user_id=db_user.id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_by_id(post_id: int, db: Session):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def update(post_id: int, post: _schemas_post.PostUpdate, email: str, db: Session):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Email user not found")

    if post.category_id != None:
        db_category = db.query(models.Category).filter(models.Category.id == post.category_id).first()
        if not db_category:
            raise HTTPException(status_code=400, detail=f"Category not found")

    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        return None

    if db_user.id != db_post.user_id:
        raise HTTPException(status_code=400, detail=f"User is not the owner of the post")

    for key, value in post.model_dump(exclude_unset=True).items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


def remove(post_id: int, email: str, db: Session):
    db_user = db.query(models.User).filter(models.User.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Email user not found")

    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        return None

    if db_user.id != db_post.user_id:
        raise HTTPException(status_code=400, detail=f"User is not the owner of the post")

    db.delete(db_post)
    db.commit()
    return  
