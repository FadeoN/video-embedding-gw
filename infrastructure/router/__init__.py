from fastapi import APIRouter

from infrastructure.controller.index import router as index_router

api_router = APIRouter()

api_router.include_router(index_router, prefix="/index", tags=["index"])