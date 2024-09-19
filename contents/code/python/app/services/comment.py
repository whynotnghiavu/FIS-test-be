from fastapi import HTTPException
from sqlalchemy.orm import Session
from ..schemas import comment as _schemas_comment



from ..models.post import Post as _models_post
from ..models.comment import Comment as _model_comment



def create(post_id: int, comment: _schemas_comment.CommentCreate, db: Session):
    db_post = db.query(_models_post).filter(_models_post.id == post_id).first()
    if not db_post:
        raise HTTPException(status_code=400, detail=f"Post not found")

    new_comment = _model_comment(post_id=post_id, **comment.model_dump())
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


def update(comment_id: int, comment: _schemas_comment.CommentUpdate, db: Session):
    if comment.post_id != None:
        db_post = db.query(_models_post).filter(_models_post.id == comment.post_id).first()
        if not db_post:
            raise HTTPException(status_code=400, detail=f"Post not found")

    db_comment = db.query(_model_comment).filter(_model_comment.id == comment_id).first()
    if db_comment is None:
        return None

    for key, value in comment.model_dump(exclude_unset=True).items():
        setattr(db_comment, key, value)
    db.commit()
    db.refresh(db_comment)
    return db_comment


def remove(comment_id: int, db: Session):
    db_comment = db.query(_model_comment).filter(_model_comment.id == comment_id).first()
    if db_comment is None:
        return None

    db.delete(db_comment)
    db.commit()
    return db_comment
