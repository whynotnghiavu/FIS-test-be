from fastapi import APIRouter, Depends, Response, status

from ..logger import setup_logger
logger = setup_logger(__name__)

router = APIRouter(prefix="/users")



@router.post('/register')
def register(
):
    # Chức năng: Đăng ký
    # Chỉ có Admin mới có thể đăng ký
    logger.info("register")
    return "register"

@router.post('/login')
def login(
):
    # Chức năng: Đăng nhập
    logger.info("login")
    return "login"