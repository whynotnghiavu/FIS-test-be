from ..logger import logger
from ..models import Base
from .engine import engine


def create_db():
    logger.warning("Creating database...")
    Base.metadata.create_all(bind=engine)
