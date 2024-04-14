from fastapi import APIRouter,Depends
from schemas.config import get_settings,Settings

router = APIRouter()

# !pong
@router.get("/ping")
async def pong(settings: Settings=Depends(get_settings)):
    return {
        "environment": settings.environment,
        "testing": settings.testing,
    }