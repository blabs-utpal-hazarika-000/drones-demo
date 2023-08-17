from fastapi import APIRouter
from .location_router import router as location_router

# Create the main router
router = APIRouter()

# Include location router
router.include_router(location_router, prefix="/v1", tags=["Location"])