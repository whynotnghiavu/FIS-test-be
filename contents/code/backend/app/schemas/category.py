from pydantic import BaseModel, field_validator
from typing import List
from .post import Post


class CategoryBase(BaseModel):
    name: str

    @field_validator("name")
    def name_not_empty(cls, name):
        if name == "":
            raise ValueError("name must not be empty")
        return name


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    posts: List[Post] = []

    class Config:
        # orm_mode = True
        from_attributes = True
