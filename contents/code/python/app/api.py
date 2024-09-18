from fastapi import FastAPI
from .routers import category
from .database import create_db


app = FastAPI(
    title='Test Kĩ Năng Backend',
)


create_db()
app.include_router(category.router, prefix="/api/v1/categories", tags=["categories"])
