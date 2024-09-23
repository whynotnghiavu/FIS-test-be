from fastapi import FastAPI

from .database.create_db import create_db
from .database.seeders.create_superuser import create_superuser


from .routers import user
from .routers import category
from .routers import post
from .routers import comment


create_db()
create_superuser()


app = FastAPI(
    title='Test Kĩ Năng Backend'
)


app.include_router(user.router, prefix=f"/api/v1", tags=["users"])
# app.include_router(category.router, prefix=f"/api/v1", tags=["categories"])
# app.include_router(post.router, prefix=f"/api/v1", tags=["posts"])
# app.include_router(comment.router, prefix=f"/api/v1", tags=["comments"])


@app.get("/")
async def root():
    return {"message": "Hello World"}
