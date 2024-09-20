from fastapi import FastAPI

from .database.create_db import create_db

from .middlewares.exception_middleware import ExceptionMiddleware

from .routers import category
from .routers import post
from .routers import comment
from .routers import user


app = FastAPI(
    title='Test Kĩ Năng Backend',
)


create_db()


app.add_middleware(ExceptionMiddleware)


app.include_router(user.router, prefix="/api/v1/user", tags=["users"])
app.include_router(category.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(post.router, prefix="/api/v1/posts", tags=["posts"])
app.include_router(comment.router, prefix="/api/v1/posts/{post_id}/comments", tags=["comments"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
