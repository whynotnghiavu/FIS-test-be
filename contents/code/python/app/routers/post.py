from fastapi import APIRouter, Depends, HTTPException,status
from sqlalchemy.orm import Session
from typing import List
from typing import Annotated


from ..database.get_db import get_db


from ..schemas import post as _schemas_post
from ..services import post as _services_post

from ..services.get_user_id import GetUserId


router = APIRouter(prefix="/posts")


@router.post("", response_model=_schemas_post.Post, status_code=status.HTTP_201_CREATED)
def create_post(
    post: _schemas_post.PostCreate,
    user_id: Annotated[str, Depends(GetUserId())],
    db: Session = Depends(get_db)
):
    return _services_post.create(post, user_id, db)


@router.get("", response_model=List[_schemas_post.Post])
def get_all_posts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return _services_post.get_all(db, skip, limit)


@router.get("/{post_id}", response_model=_schemas_post.Post)
def get_one_post_by_id(post_id: int, db: Session = Depends(get_db)):
    return _services_post.get_by_id(post_id, db)


@router.put("/{post_id}", response_model=_schemas_post.Post)
def update_post(
        post_id: int,
        post: _schemas_post.PostUpdate,
    user_id: Annotated[str, Depends(GetUserId())],
        db: Session = Depends(get_db)
):
    return _services_post.update(post_id, post, user_id, db)


@router.delete("/{post_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_post(
        post_id: int,
    user_id: Annotated[str, Depends(GetUserId())],
        db: Session = Depends(get_db)
):
    return _services_post.remove(post_id, user_id, db)
