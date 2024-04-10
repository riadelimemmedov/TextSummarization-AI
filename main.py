from fastapi import APIRouter, FastAPI,Depends
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager
from schemas.config import get_settings,Settings
from middleware.metric import metric_middleware

# Creat FastAPI object
app = FastAPI()

#Set middleware for app
app.middleware('http')(metric_middleware)


# !pong
@app.get("/ping")
async def pong(settings: Settings=Depends(get_settings)):
    return {
        "ping": "pong!",
        "environment": settings.environment,
        "testing": settings.testing
    }