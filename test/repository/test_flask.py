import pytest
from controller.main import create_app


# https://flask.palletsprojects.com/en/2.2.x/testing/
@pytest.fixture()
def application():
    test_app = create_app()
    test_app.config.update({"TESTING": True})

    yield test_app


@pytest.fixture()
def client(application):
    return application.test_client()


@pytest.fixture()
def runner(application):
    return application.test_cli_runner()


def test_request_example(client):
    response = client.get("/")
    assert b"<h1>FLASK-API-REST Olivanders</h1>" in response.data
    assert response.status_code == 200


def test_get_item(client):
    result = {
        "name": "+5 Dexterity Vest",
        "sell_in": 10,
        "quality": 20
    }

    response = client.post("/items/1")
    assert response.get_json() == result
    assert response.status_code == 200


def test_get_bad_item(client):
    result = {
        "message": "The item with 1223123123 doesn't exist"
    }

    response = client.post("/items/1223123123")
    assert response.get_json() == result
    assert response.status_code == 404


def test_post_item(client):
    item = {
        "_id": 99999,
        "name": "Test object",
        "sell_in": 1099,
        "quality": 2000
    }

    response = client.put("/items/insert/", json=item)
    assert response.status_code == 200


def test_post_fail_item(client):
    item = {
        "_id": "this is not number",
        "name": "Test object",
        "sell_in": 1099,
        "quality": 2000
    }
    response = client.put("/items/insert/", json=item)
    assert response.status_code == 400
