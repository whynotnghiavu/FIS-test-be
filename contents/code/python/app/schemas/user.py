from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from ..models import Role


class UserBase(BaseModel):
    email: str
    password: str
    role: Role


class UserLogin(UserBase):
    email: str
    password: str


class UserRegister(UserBase):
    pass


class JWTUser(UserBase):
    email: str
    role: Role


class User(UserBase):
    id: int

    class Config:
        # orm_mode = True
        from_attributes = True
