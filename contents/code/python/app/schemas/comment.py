from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime


class CommentBase(BaseModel):
    text: str

    @field_validator("text")
    def text_not_empty(cls, text):
        if text == "":
            raise ValueError("text must not be empty")

        return text


class CommentCreate(CommentBase):
    pass


class CommentUpdate(CommentBase):
    pass


class Comment(CommentBase):
    id: int
    created_at: datetime
    
    post_id: Optional[int]
    user_id: int

    class Config:
        # orm_mode = True
        from_attributes = True
