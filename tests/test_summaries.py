import json
from .infrastructure.data_clear import TruncateTestData
from models.text_summary_model import TextSummary
import pytest

@pytest.fixture
def delete_text_summaries(test_app_with_db):
    response = test_app_with_db.delete("/summaries/")
    assert response.status_code == 204
    assert response.json() == {"message": "All summaries deleted successfully"}
    return response.json()
    

def test_create_summary(test_app_with_db,delete_text_summaries):
    message = delete_text_summaries
    response = test_app_with_db.post("/summaries/", data=json.dumps({"url": "https://foo.bar/"}))
    assert response.status_code == 201
    assert response.json() == {
        "id": 1,
        "url": "https://foo.bar/",
    }