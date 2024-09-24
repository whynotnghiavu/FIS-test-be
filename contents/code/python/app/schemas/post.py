# from pydantic import BaseModel, field_validator
# from datetime import datetime
# from typing import List, Optional
# from .comment import Comment


# class PostBase(BaseModel):
#     title: str
#     content: str
#     category_id: Optional[int]

#     @field_validator("title")
#     def title_not_empty(cls, title):
#         if title == "":
#             raise ValueError("title must not be empty")

#         return title

#     @field_validator("content")
#     def content_not_empty(cls, content):
#         if content == "":
#             raise ValueError("content must not be empty")

#         return content


# class PostCreate(PostBase):
#     pass


# class PostUpdate(PostBase):
#     pass


# class Post(PostBase):
#     id: int
#     created_at: datetime

#     comments: List[Comment] = []

#     user_id: int

#     class Config:
#         # orm_mode = True
#         from_attributes = True
