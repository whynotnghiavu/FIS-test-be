from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import comment as _schemas_comment


from ..models.post import Post as _models_post
from ..models.comment import Comment as _model_comment
from ..models.user import User as _model_user


def create(post_id: int, comment: _schemas_comment.CommentCreate, email: str, db: Session):
    db_user = db.query(_model_user).filter(_model_user.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Email user not found")

    db_post = db.query(_models_post).filter(_models_post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=400, detail=f"Post not found")

    new_comment = _model_comment(user_id=db_user.id, post_id=post_id, **comment.model_dump())
    db.add(new_comment)
    db.commit()
    db.refresh(new_comment)
    return new_comment


def get_all(post_id: int, db: Session, skip: int = 0, limit: int = 100):
    db_post = db.query(_models_post).filter(_models_post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=400, detail=f"Post not found")

    return db.query(_model_comment).filter(_model_comment.post_id == post_id).offset(skip).limit(limit).all()


def get_by_id(comment_id: int, db: Session):
    return db.query(_model_comment).filter(_model_comment.id == comment_id).first()


def update(comment_id: int, comment: _schemas_comment.CommentUpdate, email: str, db: Session):
    db_user = db.query(_model_user).filter(_model_user.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Email user not found")

    if comment.post_id != None:
        db_post = db.query(_models_post).filter(_models_post.id == comment.post_id).first()
        if not db_post:
            raise HTTPException(status_code=400, detail=f"Post not found")

    db_comment = db.query(_model_comment).filter(_model_comment.id == comment_id).first()
    if db_comment is None:
        return None

    if db_user.id != db_comment.user_id:
        raise HTTPException(status_code=400, detail=f"User is not the owner of the comment")

    for key, value in comment.model_dump(exclude_unset=True).items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def remove(comment_id: int, email: str, db: Session):
    db_user = db.query(_model_user).filter(_model_user.email == email).first()
    if not db_user:
        raise HTTPException(status_code=400, detail=f"Email user not found")

    db_comment = db.query(_model_comment).filter(_model_comment.id == comment_id).first()
    if db_comment is None:
        return None

    if db_user.id != db_comment.user_id:
        raise HTTPException(status_code=400, detail=f"User is not the owner of the comment")

    db.delete(db_comment)
    db.commit()
    return db_comment
