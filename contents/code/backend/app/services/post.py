from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..schemas import post as _schemas_post

from .. import models


def create(post: _schemas_post.PostCreate, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    db_category = db.query(models.Category).filter(models.Category.id == post.category_id).first()
    if not db_category:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category not found")

    new_post = models.Post(user_id=user_id, **post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_by_id(post_id: int, db: Session):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def update(post_id: int, post: _schemas_post.PostUpdate, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    if post.category_id != None:
        db_category = db.query(models.Category).filter(models.Category.id == post.category_id).first()
        if not db_category:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Category not found")

    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if db_post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User is not the owner of the post")

    for key, value in post.model_dump(exclude_unset=True).items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


def remove(post_id: int, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Post not found")

    if db_post.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User is not the owner of the post")

    db.delete(db_post)
    db.commit()
    return
