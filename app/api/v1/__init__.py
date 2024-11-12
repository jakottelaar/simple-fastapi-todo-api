from fastapi import APIRouter

from app.api.v1.todos import router as todos_router
from app.api.v1.health import router as health_router

router = APIRouter(prefix="/v1")
router.include_router(todos_router)
router.include_router(health_router)