from pydantic import BaseModel





class CategoryBase(BaseModel):
    name: str


class CategoryCreate(CategoryBase):
    pass


class CategoryUpdate(CategoryBase):
    pass


class Category(CategoryBase):
    id: int
    # posts: List[Post] = []

    class Config:
        # orm_mode = True
        from_attributes = True