from fastapi import APIRouter
from .blog import router as blog_router
from .user_process import router as user_router
api_router = APIRouter()
api_router.include_router(blog_router, prefix="")
api_router.include_router(user_router, prefix="")
