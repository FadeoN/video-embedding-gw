from fastapi import APIRouter

from infrastructure.controller.index import router as index_router
from infrastructure.controller.similarity import router as similarity_router

api_router = APIRouter()

api_router.include_router(index_router, prefix="/index", tags=["index"])
api_router.include_router(similarity_router, prefix="/similarities", tags=["similarity"])