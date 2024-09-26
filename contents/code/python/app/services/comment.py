from fastapi import HTTPException, status
from sqlalchemy.orm import Session

from ..schemas import comment as _schemas_comment

from .. import models


def create(post_id: int, comment: _schemas_comment.CommentCreate, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found")

    new_comment = models.Comment(user_id=user_id, post_id=post_id, **comment.model_dump())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(post_id: int, db: Session, skip: int = 0, limit: int = 100):
    db_post = db.query(models.Post).filter(models.Post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found")

    return db.query(models.Comment).filter(models.Comment.post_id == post_id).offset(skip).limit(limit).all()


def get_by_id(comment_id: int, db: Session):
    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")
    return db.query(models.Comment).filter(models.Comment.id == comment_id).first()


def update(comment_id: int, comment: _schemas_comment.CommentUpdate, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    if comment.post_id != None:
        db_post = db.query(models.Post).filter(models.Post.id == comment.post_id).first()
        if not db_post:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Post not found")

    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if not db_comment:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    if db_comment.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User is not the owner of the comment")

    for key, value in comment.model_dump(exclude_unset=True).items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def remove(comment_id: int, user_id: int, db: Session):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    if not db_user:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"User not found")

    db_comment = db.query(models.Comment).filter(models.Comment.id == comment_id).first()
    if db_comment is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Comment not found")

    if db_comment.user_id != user_id:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail=f"User is not the owner of the comment")

    db.delete(db_comment)
    db.commit()
    return
