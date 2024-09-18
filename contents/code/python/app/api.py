from fastapi import FastAPI
from .routers import category
from .database import create_db


app = FastAPI(
    title='Test Kĩ Năng Backend',
)


create_db()
app.include_router(category.router, prefix="/api/v1/categories", tags=["categories"])
# post
# comment



# from fastapi.security import OAuth2PasswordBearer
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# from typing import Annotated
# from fastapi import Depends
# @app.get("/items/")
# async def read_items(token: Annotated[str, Depends(oauth2_scheme)]):
#     return {"token": token}