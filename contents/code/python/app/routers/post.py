from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List



from ..database.get_db import get_db



from ..schemas import post as _schemas_post
from ..services import post as _services_post


router = APIRouter()


@router.post("", response_model=_schemas_post.Post)
def create_post(post: _schemas_post.PostCreate, db: Session = Depends(get_db)):
    return _services_post.create(post, db)


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
def update_post(post_id: int, post: _schemas_post.PostUpdate, db: Session = Depends(get_db)):
    updated_post = _services_post.update(post_id, post, db)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post


@router.delete("/{post_id}", response_model=_schemas_post.Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = _services_post.remove(post_id, db)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
