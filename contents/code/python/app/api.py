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

api_version = "/api/v1"

app.include_router(user.router, prefix=f"{api_version}", tags=["users"])
app.include_router(category.router, prefix=f"{api_version}", tags=["categories"])
app.include_router(post.router, prefix=f"{api_version}", tags=["posts"])
app.include_router(comment.router, prefix=f"{api_version}", tags=["comments"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
