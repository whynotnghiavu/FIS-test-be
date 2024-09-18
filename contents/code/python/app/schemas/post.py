from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional
from .comment import Comment




class PostBase(BaseModel):
    title: str
    content: str
    created_at: datetime
    category_id: Optional[int]


class PostCreate(PostBase):
    pass


class PostUpdate(PostBase):
    pass


class Post(PostBase):
    id: int
    comments: List[Comment] = []

    class Config:
        # orm_mode = True
        from_attributes = True


