from ..models.base import Base
from .engine import engine


def create_db():
    Base.metadata.create_all(bind=engine)
