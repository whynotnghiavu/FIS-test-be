from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from ..database import get_db
from ..schemas import comment as _schemas_comment
from ..services import comment as _services_comment


router = APIRouter()


@router.post("", response_model=_schemas_comment.Comment)
def create_comment(post_id: int, comment: _schemas_comment.CommentCreate, db: Session = Depends(get_db)):
    return _services_comment.create(post_id, comment, db)


@router.get("", response_model=List[_schemas_comment.Comment])
def get_all_comments(post_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return _services_comment.get_all(post_id, db, skip, limit)


@router.get("/{comment_id}", response_model=_schemas_comment.Comment)
def get_one_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    comment = _services_comment.get_by_id(comment_id, db)
    if comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return comment


@router.put("/{comment_id}", response_model=_schemas_comment.Comment)
def update_comment(comment_id: int, comment: _schemas_comment.CommentUpdate, db: Session = Depends(get_db)):
    updated_comment = _services_comment.update(comment_id, comment, db)
    if updated_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return updated_comment


@router.delete("/{comment_id}", response_model=_schemas_comment.Comment)
def delete_comment(comment_id: int, db: Session = Depends(get_db)):
    deleted_comment = _services_comment.remove(comment_id, db)
    if deleted_comment is None:
        raise HTTPException(status_code=404, detail="Comment not found")
    return deleted_comment
