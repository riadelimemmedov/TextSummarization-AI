import logging
from contextlib import asynccontextmanager

from fastapi import APIRouter, Depends, FastAPI

from api import ping
from database.config import init_db
from middleware.middlewares import init_middleware
from resources.routes import api_router

# Create FastAPI object
app = FastAPI()


# Created log object for uvicorn services,which is gateway for backend and frontend services.
log = logging.getLogger("uvicorn")


#! create_application
def create_application() -> FastAPI:
    # ? Create fastaapi instance from FastAPI object
    application = FastAPI()

    # ? Registered url resources to root url of this application
    application.include_router(api_router)

    return application


# ? Create fastaapi application
app = create_application()

# ? Start middleware
init_middleware(app)


@app.on_event("startup")
async def startup_event():
    log.info("Starting up...")
    init_db(app)


@app.on_event("shutdown")
async def shutdown_event():
    log.info("Shutting down...")
