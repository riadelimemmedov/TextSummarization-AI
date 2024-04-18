import os
from fastapi import FastAPI
from tortoise.contrib.fastapi import register_tortoise
from tortoise import Tortoise, run_async 
import logging

log = logging.getLogger("uvicorn")

#? Create a tortoise orm object
TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["models.text_summary_model", "aerich.models"],
            "default_connection": "default",
        },
    },
}

#! init_db
def init_db(app:FastAPI) -> None:
    register_tortoise(app,db_url=os.environ.get("DATABASE_URL"),modules={"models": ["models.text_summary_model"]},generate_schemas=False,add_exception_handlers=True)


#! init_test_db
def init_test_db(app:FastAPI) -> None:
    register_tortoise(app,db_url=os.environ.get("DATABASE_TEST_URL"),modules={"models": ["models.text_summary_model"]},generate_schemas=True,add_exception_handlers=True)


    
#! generate_schema
async def generate_schema() -> None:
    log.info("Initializing Tortoise...")
    
    await Tortoise.init(
        config=TORTOISE_ORM
    )
    log.info("Generating database schema via Tortoise...")
    await Tortoise.generate_schemas()
    await Tortoise.close_connections()
    

#! run function only inside this module
if __name__ == "__main__":
    run_async(generate_schema())
