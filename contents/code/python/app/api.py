from fastapi import FastAPI

from .database.create_db import create_db
from .database.seeders.create_superuser import create_superuser


create_db()
create_superuser()


app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}
