import os
import time
from sqlalchemy import create_engine
from sqlalchemy.exc import OperationalError


MYSQL_HOST = os.getenv("MYSQL_HOST") or "localhost"

MYSQL_PORT = os.getenv("MYSQL_PORT") or "3306"
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE") or "nghia"

MYSQL_USERNAME = os.getenv("MYSQL_USERNAME") or "root"
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD") or ""

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'

MYSQL_CONNECT_RETRIES = os.getenv("MYSQL_CONNECT_RETRIES") or 5
MYSQL_CONNECT_RETRY_DELAY = os.getenv("MYSQL_CONNECT_RETRY_DELAY") or 5


def connect_with_retry():
    attempt = 0
    while attempt < MYSQL_CONNECT_RETRIES:
        try:
            engine = create_engine(
                SQLALCHEMY_DATABASE_URL,
                pool_pre_ping=True  # Thực hiện ping câu truy vấn đơn giản
            )
            engine.connect()
            print("Connection successful!")
            return engine
        except OperationalError:
            attempt += 1
            print(f"Connection failed. Retrying in {MYSQL_CONNECT_RETRY_DELAY} seconds... ({attempt}/{MYSQL_CONNECT_RETRIES})")
            time.sleep(MYSQL_CONNECT_RETRY_DELAY)
    raise Exception(f"Failed to connect after {MYSQL_CONNECT_RETRIES} attempts.")


engine = connect_with_retry()

