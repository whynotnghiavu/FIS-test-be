from fastapi import HTTPException, Request
from starlette.middleware.base import BaseHTTPMiddleware
from fastapi.responses import JSONResponse
from sqlalchemy.exc import SQLAlchemyError


class ExceptionMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        try:
            response = await call_next(request)
            return response
        except SQLAlchemyError as e:
            print(f"Database error occurred: {e}")
            return JSONResponse(
                status_code=500,
                content={"detail": "Connection to the database failed"},
            )
        except Exception as e:
            print(f"An unexpected error occurred: {e}")
            return JSONResponse(
                status_code=500,
                content={"detail": "A server error occurred."},
            )
