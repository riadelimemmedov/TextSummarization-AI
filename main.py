from fastapi import APIRouter, FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from schemas.config import get_settings,Settings
from middleware.metric import metric_middleware
from tortoise.contrib.fastapi import register_tortoise
from database.config import TORTOISE_ORM

# Create FastAPI object
app = FastAPI()

#Set middleware for app
app.middleware('http')(metric_middleware)

#Connect tortoise orm to api
register_tortoise(app,config=TORTOISE_ORM,generate_schemas=False,add_exception_handlers=True)

# !pong
@app.get("/ping")
async def pong(settings: Settings=Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing,
        "db_url": settings.database_url
    }