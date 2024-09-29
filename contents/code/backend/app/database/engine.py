import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError
from sqlalchemy import URL


from ..logger import setup_logger
logger = setup_logger(__name__)

SQLALCHEMY_DATABASE_URL = URL.create(
    drivername="mysql+pymysql",
    username=os.getenv("MYSQL_USERNAME", "root"),
    password=os.getenv("MYSQL_PASSWORD", ""),
    host=os.getenv("MYSQL_HOST", "localhost"),
    port=os.getenv("MYSQL_PORT", "3306"),
    database=os.getenv("MYSQL_DATABASE", "nghia")
).render_as_string(hide_password=False)


MYSQL_CONNECT_RETRIES = int(os.getenv("MYSQL_CONNECT_RETRIES", 5))
MYSQL_CONNECT_RETRY_DELAY = int(os.getenv("MYSQL_CONNECT_RETRY_DELAY", 5))


def connect_with_retry():
    attempt = 0
    while attempt < MYSQL_CONNECT_RETRIES:
        try:
            engine = create_engine(
                SQLALCHEMY_DATABASE_URL,
                # echo=True, # Hiển thị log SQL
                pool_pre_ping=True  # Thực hiện ping mỗi câu truy vấn
            )
            engine.connect()
            logger.warning("Connection successful!")
            return engine
        except OperationalError:
            attempt += 1
            logger.warning(f"Connection failed. Retrying in {MYSQL_CONNECT_RETRY_DELAY} seconds... ({attempt}/{MYSQL_CONNECT_RETRIES})")
            time.sleep(MYSQL_CONNECT_RETRY_DELAY)
    raise Exception(f"Failed to connect after {MYSQL_CONNECT_RETRIES} attempts.")


engine = connect_with_retry()
