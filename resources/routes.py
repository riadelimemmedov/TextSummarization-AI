from fastapi import APIRouter

from api.summarie import summaries

api_router = APIRouter()
api_router.include_router(summaries.router)