from fastapi import FastAPI
from .database import create_db
from .routers import category
from .routers import post


app = FastAPI(
    title='Test Kĩ Năng Backend',
)


create_db()
app.include_router(category.router, prefix="/api/v1/categories", tags=["categories"])
app.include_router(post.router, prefix="/api/v1/posts", tags=["posts"])
# comment





# from fastapi.security import OAuth2PasswordBearer
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# from typing import Annotated
# from fastapi import Depends
# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}