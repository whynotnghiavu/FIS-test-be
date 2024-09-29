from ..models import Base
from .engine import engine


from ..logger import setup_logger
logger = setup_logger(__name__)


def create_db():
    logger.warning("Creating database...")
    Base.metadata.create_all(bind=engine)
