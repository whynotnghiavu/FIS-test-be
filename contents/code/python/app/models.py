from enum import Enum
import sqlalchemy as _sqlalchemy
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


from datetime import datetime


Base = declarative_base()


class Category(Base):
    __tablename__ = "categories"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    name = _sqlalchemy.Column(_sqlalchemy.String(255), unique=True, index=True)
    description = _sqlalchemy.Column(_sqlalchemy.String(255), unique=True, index=True)

    posts = relationship("Post", back_populates="category", cascade="all, delete-orphan")


class Post(Base):
    __tablename__ = "posts"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    title = _sqlalchemy.Column(_sqlalchemy.String(255), index=True)
    content = _sqlalchemy.Column(_sqlalchemy.Text)
    created_at = _sqlalchemy.Column(_sqlalchemy.DateTime(timezone=True), default=datetime.now())

    user_id = _sqlalchemy.Column(_sqlalchemy.Integer, _sqlalchemy.ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    category_id = _sqlalchemy.Column(_sqlalchemy.Integer, _sqlalchemy.ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)

    user = relationship("User", back_populates="posts")
    category = relationship("Category", back_populates="posts")
    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")


class Comment(Base):
    __tablename__ = "comments"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    text = _sqlalchemy.Column(_sqlalchemy.Text)
    created_at = _sqlalchemy.Column(_sqlalchemy.DateTime(timezone=True), default=datetime.now())

    user_id = _sqlalchemy.Column(_sqlalchemy.Integer, _sqlalchemy.ForeignKey("users.id", ondelete="CASCADE"), nullable=True)
    post_id = _sqlalchemy.Column(_sqlalchemy.Integer, _sqlalchemy.ForeignKey("posts.id", ondelete="SET NULL"), nullable=True)

    user = relationship("User", back_populates="comments")
    post = relationship("Post", back_populates="comments")


class Role(str, Enum):
    ADMIN = "admin"
    USER = "user"


class User(Base):
    __tablename__ = "users"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    email = _sqlalchemy.Column(_sqlalchemy.String(255), unique=True, nullable=False, index=True)
    password = _sqlalchemy.Column(_sqlalchemy.String(255), nullable=False)
    role = _sqlalchemy.Column(_sqlalchemy.Enum(Role))

    posts = relationship("Post", back_populates="user", cascade="all, delete-orphan")
    comments = relationship("Comment", back_populates="user", cascade="all, delete-orphan")
