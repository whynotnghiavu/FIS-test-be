from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from typing import Annotated


from ..database.get_db import get_db


from ..schemas import comment as _schemas_comment

from ..services import comment as _services_comment

from ..services.get_user_id import GetUserId
from ..services.auth import validate_otp


router = APIRouter(prefix="/posts/{post_id}/comments")


@router.post("", response_model=_schemas_comment.Comment, status_code=status.HTTP_201_CREATED)
def create_comment(
    post_id: int,
    comment: _schemas_comment.CommentCreate,
    user_id: Annotated[str, Depends(GetUserId())],
    _otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):
    return _services_comment.create(post_id, comment, user_id, db)


@router.get("", response_model=List[_schemas_comment.Comment])
def get_all_comments(post_id: int, db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return _services_comment.get_all(post_id, db, skip, limit)


@router.get("/{comment_id}", response_model=_schemas_comment.Comment)
def get_one_comment_by_id(comment_id: int, db: Session = Depends(get_db)):
    return _services_comment.get_by_id(comment_id, db)


@router.put("/{comment_id}", response_model=_schemas_comment.Comment)
def update_comment(
    comment_id: int,
    comment: _schemas_comment.CommentUpdate,
    user_id: Annotated[str, Depends(GetUserId())],
    _otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):
    return _services_comment.update(comment_id, comment, user_id, db)


@router.delete("/{comment_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_comment(
    comment_id: int,
    user_id: Annotated[str, Depends(GetUserId())],
    _otp: Annotated[bool, Depends(validate_otp)],
    db: Session = Depends(get_db)
):

    return _services_comment.remove(comment_id, user_id, db)
