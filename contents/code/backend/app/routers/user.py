from fastapi import APIRouter, Depends, Response, status

from ..logger import setup_logger
logger = setup_logger(__name__)

router = APIRouter(prefix="/users")



@router.post('/register')
def register(
):
    logger.info("register")
    return "register"

@router.post('/login')
def login(
):
    logger.info("login")
    return "login"