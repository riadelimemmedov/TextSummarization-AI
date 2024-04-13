import os


TORTOISE_ORM = {
    "connections": {"default": os.environ.get("DATABASE_URL")},
    "apps": {
        "models": {
            "models": ["models.text_summary_model", "aerich.models"],
            "default_connection": "default",
        },
    },
}