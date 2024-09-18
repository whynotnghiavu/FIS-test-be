from sqlalchemy import Column, ForeignKey, Integer, String, Text, DateTime
from .database import Base

class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    # posts = relationship("Post", back_populates="category")