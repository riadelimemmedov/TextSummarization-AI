import json

import pytest

from models.text_summary_model import TextSummary

from .infrastructure.data_clear import TruncateTestData


@pytest.fixture
def create_summary(test_app_with_db):
    """
    Pytest fixture that creates a summary by making a POST request to the "/summaries/" endpoint.

    Args:
        test_app_with_db: Test client for the FastAPI application with a test database.

    Yields:
        The response object containing the created summary.
    """
    created_summaries_response = test_app_with_db.post(
        "/summaries/", data=json.dumps({"url": "https://foo.bar/"})
    )
    yield created_summaries_response


def test_read_all_summaries(test_app_with_db, create_summary):
    """
    Test function to verify the behavior of reading all summaries.

    Args:
        test_app_with_db (TestClient): The test client with a connected test database.
        create_summary (fixture): A fixture that creates a summary and returns the response.

    Returns:
        None

    Raises:
        AssertionError: If the response status code is not 200 or
                        if the summary with the specified ID is not found in the response.

    """
    created_summaries_response = create_summary
    summary_id = created_summaries_response.json()["id"]

    response = test_app_with_db.get("/summaries/")
    assert response.status_code == 200

    response_list = response.json()
    assert len(list(filter(lambda d: d["id"] == summary_id, response_list))) == 1


def test_read_summary(test_app_with_db, create_summary):
    """
    Test case to verify the successful retrieval of a summary.

    Args:
        test_app_with_db: The test client for the application with the database.
        create_summary: The response object containing the created summary.

    Raises:
        AssertionError: If any of the assertions fail, indicating unexpected behavior.

    Returns:
        None
    """
    created_summaries_response = create_summary
    summary_id = created_summaries_response.json()["id"]
    assert summary_id is not None

    response = test_app_with_db.get(f"/summaries/{summary_id}/")
    assert response.status_code == 200

    response_dict = response.json()
    assert response_dict["id"] == summary_id
    assert response_dict["summary"]
    assert response_dict["created_at"]


def test_read_summary_incorrect_id(test_app_with_db):
    """
    Test case to verify that a 404 error is returned when trying to retrieve a summary with an incorrect ID.

    Args:
        test_app_with_db: The test client for the application with the database.

    Raises:
        AssertionError: If the response status code is not 404 or the response detail is not "Summary not found".
    """
    response = test_app_with_db.get("/summaries/999/")
    assert response.status_code == 404
    assert response.json()["detail"] == "Summary not found"


def test_delete_text_summaries(test_app_with_db):
    """
    Test case to verify the behavior of deleting all text summaries.

    Args:
        test_app_with_db: Test client for the FastAPI application with a test database.

    Raises:
        AssertionError: If the response status code is not 202 or the response JSON is not as expected.
    """
    response = test_app_with_db.delete("/summaries/")
    assert response.status_code == 202
    assert response.json() == {"message": "All summaries deleted successfully"}


def test_create_summary(test_app_with_db, create_summary):
    """
    Test case to verify the behavior of creating a summary.

    Args:
        test_app_with_db: Test client for the FastAPI application with a test database.
        create_summary: Fixture that creates a summary by making a POST request to the "/summaries/" endpoint.

    Raises:
        AssertionError: If the response status code is not 201 or the response JSON is not as expected.
    """
    created_summaries_response = create_summary
    assert created_summaries_response.status_code == 201
    assert created_summaries_response.json()["url"] == "https://foo.bar/"


def test_create_summaries_invalid_json(test_app):
    """
    Test case to verify the behavior of creating summaries with invalid JSON data.

    Args:
        test_app: Test client for the FastAPI application.

    Raises:
        AssertionError: If the response status code is not 422 or the response JSON is not as expected.
    """
    response = test_app.post("/summaries/", data=json.dumps({}))
    assert response.status_code == 422
    assert response.json() == {
        "detail": [
            {
                "type": "missing",
                "loc": ["body", "url"],
                "msg": "Field required",
                "input": {},
                "url": "https://errors.pydantic.dev/2.7/v/missing",
            }
        ]
    }
