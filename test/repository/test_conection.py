import pytest
import requests

@pytest.mark.test_conectiondb
def test_mongodb_ping():
    atlas_url = "https://cloud.mongodb.com/"

    # Try to make request
    try:
        response = requests.get(atlas_url)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        pytest.fail("No hay conexión con mongodbCloud")

    # Check HTTP code response
    assert response.status_code == 200




