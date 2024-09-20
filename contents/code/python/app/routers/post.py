from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List
from typing import Annotated


from ..database.get_db import get_db


from ..schemas import post as _schemas_post
from ..services import post as _services_post
from ..services.get_email_user import GetEmailUser


router = APIRouter(prefix="/posts")


@router.post("", response_model=_schemas_post.Post)
def create_post(
    post: _schemas_post.PostCreate,
    email: Annotated[str, Depends(GetEmailUser())],
    db: Session = Depends(get_db)
):
    return _services_post.create(post, email, db)


@router.get("", response_model=List[_schemas_post.Post])
def get_all_posts(db: Session = Depends(get_db), skip: int = 0, limit: int = 100):
    return _services_post.get_all(db, skip, limit)


@router.get("/{post_id}", response_model=_schemas_post.Post)
def get_one_post_by_id(post_id: int, db: Session = Depends(get_db)):
    post = _services_post.get_by_id(post_id, db)
    if post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return post


@router.put("/{post_id}", response_model=_schemas_post.Post)
def update_post(
    post_id: int,
    post: _schemas_post.PostUpdate,
    email: Annotated[str, Depends(GetEmailUser())],
    db: Session = Depends(get_db)
):
    updated_post = _services_post.update(post_id, post, email, db)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


@router.delete("/{post_id}", status_code=204)
def delete_post(
    post_id: int,
    email: Annotated[str, Depends(GetEmailUser())],
    db: Session = Depends(get_db)
):
    deleted_post = _services_post.remove(post_id, email, db)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return  
