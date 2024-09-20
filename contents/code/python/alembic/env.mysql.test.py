import os 
from dotenv import load_dotenv
 
FILE_ENV = "../../docker/.env"
# load_dotenv(FILE_ENV)







MYSQL_HOST = os.getenv("MYSQL_HOST", "localhost")
print(f"🚀 {MYSQL_HOST}")


MYSQL_PORT = os.getenv("MYSQL_PORT", "3306")
print(f"🚀 {MYSQL_PORT}")
MYSQL_DATABASE = os.getenv("MYSQL_DATABASE", "nghia")
print(f"🚀 {MYSQL_DATABASE}")


MYSQL_USERNAME = os.getenv("MYSQL_USERNAME", "root")
print(f"🚀 {MYSQL_USERNAME}")
MYSQL_PASSWORD = os.getenv("MYSQL_PASSWORD", "")
print(f"🚀 {MYSQL_PASSWORD}")


SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{MYSQL_USERNAME}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DATABASE}'
print(f"🚀 {SQLALCHEMY_DATABASE_URL}")



