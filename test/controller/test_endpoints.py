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


def test_request_example(client):
    response = client.get("/")
    assert b"<h1>FLASK-API-REST Olivanders</h1>" in response.data
    assert response.status_code == 200


def test_get_item(client):
    response = client.get("/items/1")
    assert response.status_code == 200


def test_get_bad_item(client):
    result = {
        "message": "The item with 1223123123 doesn't exist"
    }
    response = client.get("/items/1223123123")
    assert response.get_json() == result
    assert response.status_code == 404


def test_put_item(client):
    item = {
        "_id": 999,
        "name": "Test object",
        "sell_in": 1099,
        "quality": 2000
    }
    response = client.put("/items/insert/", json=item)
    assert response.status_code == 200
    assert response.get_json() == {"Message": "The item has been introduced with id 999"}


def test_put_repetedItem(client):
    item = {
        "_id": 999,
        "name": "Test object",
        "sell_in": 1099,
        "quality": 2000
    }

    response = client.put("/items/insert/", json=item)
    assert response.status_code == 200
    assert response.get_json() == {"Message": "The item has not been introduced, maybe is already at the DB"}


def test_put_fail_item(client):
    item = {
        "_id": "this is not number",
        "name": "Test object",
        "sell_in": 1099,
        "quality": 2000
    }
    response = client.put("/items/insert/", json=item)
    assert response.status_code == 400


def test_delete_existingItem(client):
    response = client.delete("/items/delete/999")
    assert response.status_code == 200
    assert response.get_json() == {"Message": "The item has been deleted with id 999"}


def test_delete_notExistingItem(client):
    response = client.delete("/items/delete/999")
    assert response.status_code == 200
    assert response.get_json() == {"Message": "The item is not in the DB"}

def test_get_getAllItems(client):
    response = client.get("/items/all")
    assert response.status_code == 200


def test_get_updateAllItems(client):
    response = client.get("/db/update")
    assert response.status_code == 200
