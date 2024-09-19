from ..database import Base
import sqlalchemy as _sqlalchemy
from sqlalchemy.orm import relationship

from datetime import datetime

 
class Comment(Base):
    __tablename__ = "comments"

    id = _sqlalchemy.Column(_sqlalchemy.Integer, primary_key=True, index=True)
    text = _sqlalchemy.Column(_sqlalchemy.Text)
    created_at = _sqlalchemy.Column(_sqlalchemy.DateTime(timezone=True), default=datetime.now())
    post_id = _sqlalchemy.Column(_sqlalchemy.Integer, _sqlalchemy.ForeignKey("posts.id", ondelete="SET NULL"), nullable=True)

    post = relationship("Post", back_populates="comments")
