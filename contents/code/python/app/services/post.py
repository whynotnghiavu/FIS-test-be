from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import post as _schemas_post
from .. import models


def create(post: _schemas_post.PostCreate, db: Session):
    db_category = db.query(models.Category).filter(models.Category.id == post.category_id).first()
    if not db_category:
        raise HTTPException(status_code=400, detail=f"Category not found")

    new_post = models.Post(**post.model_dump())
    db.add(new_post)
    db.commit()
    db.refresh(new_post)
    return new_post


def get_all(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Post).offset(skip).limit(limit).all()


def get_by_id(post_id: int, db: Session):
    return db.query(models.Post).filter(models.Post.id == post_id).first()


def update(post_id: int, post: _schemas_post.PostUpdate, db: Session):
    if post.category_id != None:
        db_category = db.query(models.Category).filter(models.Category.id == post.category_id).first()
        if not db_category:
            raise HTTPException(status_code=400, detail=f"Category not found")

    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_post is None:
        return None

    for key, value in post.model_dump(exclude_unset=True).items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post


def remove(post_id: int, db: Session):
    db_category = db.query(models.Post).filter(models.Post.id == post_id).first()
    if db_category is None:
        return None

    db.delete(db_category)
    db.commit()
    return db_category
