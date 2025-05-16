from fastapi import APIRouter
from .password import router as password_router
from .student import router as register_router

router = APIRouter()

router.include_router(password_router)
router.include_router(register_router)