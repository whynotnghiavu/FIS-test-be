from ..database import Base
import sqlalchemy as _sqlalchemy
from sqlalchemy.orm import relationship

from datetime import datetime

 

class Post(Base):
    __tablename__ = "posts"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    title = _sqlalchemy.Column(_sqlalchemy.String(255), index=True)
    content = _sqlalchemy.Column(_sqlalchemy.Text)
    created_at = _sqlalchemy.Column(_sqlalchemy.DateTime(timezone=True), default=datetime.now())
    category_id = _sqlalchemy.Column(_sqlalchemy.Integer, _sqlalchemy.ForeignKey("categories.id", ondelete="SET NULL"), nullable=True)

    category = relationship("Category", back_populates="posts")

    comments = relationship("Comment", back_populates="post", cascade="all, delete-orphan")
