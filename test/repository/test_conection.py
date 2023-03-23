import pytest
import requests


@pytest.mark.test_db
def test_mongodb_ping():
    atlas_url = "https://cloud.mongodb.com/"

    response = requests.get(atlas_url)
    response.raise_for_status()

    # Check HTTP code response
    assert response.status_code == 200
