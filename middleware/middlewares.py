from fastapi import FastAPI
from .metric import metric_middleware

#! init_middleware
def init_middleware(app:FastAPI) -> None:
    app.middleware('http')(metric_middleware)