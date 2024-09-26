from fastapi import FastAPI
from contextlib import asynccontextmanager
from fastapi.middleware.cors import CORSMiddleware


# from .database.create_db import create_db
# from .seeders.create_superuser import create_superuser

from .routers import user
# from .routers import category
# from .routers import post
# from .routers import comment


from .logger import setup_logger
logger = setup_logger(__name__)


def create_db():
    logger.info("create_db")


def create_superuser():
    logger.info("create_superuser")


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Code to run at application startup
    logger.info("Server is starting...")
    create_db()
    create_superuser()
    yield
    # Code to run at application shutdown
    print("Application shutdown")


app = FastAPI(
    title='Test Kĩ Năng Backend',
    lifespan=lifespan
)


# Kiến thức về CORS
origins = [
    "*",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(user.router, prefix=f"/api/v1", tags=["users"])
# app.include_router(category.router, prefix=f"/api/v1", tags=["categories"])
# app.include_router(post.router, prefix=f"/api/v1", tags=["posts"])
# app.include_router(comment.router, prefix=f"/api/v1", tags=["comments"])


@app.get("/")
def root():
    logger.info("Hello World!")
    return {"message": "Hello World"}
