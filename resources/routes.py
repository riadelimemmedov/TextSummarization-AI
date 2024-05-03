from fastapi import APIRouter

from api.summarie import summaries

# Create an APIRouter object
api_router = APIRouter()

# Include the summaries router under the "/summaries" prefix
api_router.include_router(summaries.router, prefix="/summaries")
