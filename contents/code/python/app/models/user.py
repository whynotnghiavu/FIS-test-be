from ..database.base import Base
import sqlalchemy as _sqlalchemy
from sqlalchemy.orm import relationship

from enum import Enum

from .role import Role


class User(Base):
    __tablename__ = "users"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    email = _sqlalchemy.Column(_sqlalchemy.String(255), unique=True, nullable=False, index=True)
    password = _sqlalchemy.Column(_sqlalchemy.String(255), nullable=False)
    role = _sqlalchemy.Column(_sqlalchemy.Enum(Role))

    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
