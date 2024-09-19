from ..database import Base
import sqlalchemy as _sqlalchemy
from sqlalchemy.orm import relationship


class Category(Base):
    __tablename__ = "categories"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    name = _sqlalchemy.Column(_sqlalchemy.String(255), unique=True, index=True)
    posts = relationship("Post", back_populates="category", cascade="all, delete-orphan")
