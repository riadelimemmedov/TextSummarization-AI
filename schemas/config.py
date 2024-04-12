import logging
from pydantic_settings import BaseSettings
from functools import lru_cache
import os


#Created log object for uvicorn services,which is gateway for backend and frontend services.
log = logging.getLogger("uvicorn")


# !Settings
class Settings(BaseSettings):
    """
    Represents the application settings.

    This class inherits from `BaseSettings` and provides a structured representation of the application's configuration
    settings.

    Attributes:
        environment (str): The environment in which the application is running. Defaults to "dev".
        testing (bool): A flag indicating whether the application is in testing mode. Defaults to False.

    Example:
        >>> settings = Settings()
        >>> print(settings.environment)
        dev
        >>> print(settings.testing)
        False
    """
    environment: str = os.getenv("ENVIRONMENT", "test")
    testing: bool = bool(int(os.getenv("TESTING", 0)))
    
# !get_settings
@lru_cache() 
def get_settings() -> BaseSettings:
    """
    Retrieves the configuration settings from the environment.

    This function loads the configuration settings from the environment and returns an instance of the `BaseSettings`
    class representing the settings.

    Returns:
        BaseSettings: An instance of the `BaseSettings` class containing the configuration settings.
    
    @lru_cache():
        Its a caching technique used computer science to store frequently accessed data memory, improving the overall performance of an application.

    Example:
        >>> settings = get_settings()
    """
    log.info("Loading config settings from the environment...")
    return Settings()