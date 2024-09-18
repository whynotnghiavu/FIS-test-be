from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime


class CommentBase(BaseModel):
    text: str
    created_at: datetime
    post_id: Optional[int]


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class Comment(CommentBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True
