import os

import pytest
from starlette.testclient import TestClient

from main import create_application
from schemas.config import get_settings,Settings

import os

#! get_settings_override
def get_settings_override():
    """
    Get Settings Override

    This function returns an instance of the `Settings` class with overridden values for a test environment.

    Returns:
    --------
    Settings: An instance of the `Settings` class with overridden values.

    Explanation:
    ------------
    The `get_settings_override` function is used to generate an instance of the `Settings` class with specific values for a test environment. The overridden values are as follows:

    - `environment` (str): Set to "test" to indicate the test environment.
    - `testing` (bool): Set to `True` to enable testing mode.
    - `database_url` (str): Set to the value of the "DATABASE_TEST_URL" environment variable retrieved using `os.environ.get("DATABASE_TEST_URL")`.
    """
    return Settings(environment="test",testing=bool(1), database_url=os.environ.get("DATABASE_TEST_URL"))


# !test_app
@pytest.fixture(scope="module")
def test_app():
    """
    Test App Fixture

    This pytest fixture provides a test client for the application with overridden settings.

    Returns:
    --------
    TestClient: A test client for the application.

    Explanation:
    ------------
    The `test_app` fixture is used to provide a test client for the application with overridden settings. The fixture performs the following steps:

    1. Overrides the `get_settings` dependency of the application with the `get_settings_override` function using `app.dependency_overrides`.
    2. Creates a test client for the application using `TestClient(app)`.
    3. Yields the test client to the test functions.

    The overridden settings ensure that the application uses the appropriate test environment configurations.
    """
    app = create_application()
    app.dependency_overrides[get_settings] = get_settings_override
    with TestClient(app) as test_client:
        yield test_client
