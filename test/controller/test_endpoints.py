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


@pytest.mark.test_endpoints
def test_get_AllItemsWithoutInitializeDb(client):
    response = client.get("/items/all")
    assert response.status_code == 404
@pytest.mark.test_endpoints
def test_get_UpdateAllItemsWithoutInitializeDb(client):
    response = client.get("/db/update")
    assert response.status_code == 404

@pytest.mark.test_endpoints
def test_get_intializeDb(client):
    response = client.get("/db/initialize")
    assert response.status_code == 200
    assert response.get_json() == {"Message": "GildedRose is Open!"}


@pytest.mark.test_endpoints
def test_get_Wellcome(client):
    response = client.get("/")
    assert response.get_json() == {"Message": "Flask is Running!"}
    assert response.status_code == 200


@pytest.mark.test_endpoints
def test_get_AnExistingItem(client):
    response = client.get("/items/1")
    assert response.status_code == 200


@pytest.mark.test_endpoints
def test_get_NonExistingItem(client):
    result = {"message": "The item with 1223123123 doesn't exist"}
    response = client.get("/items/1223123123")
    assert response.get_json() == result
    assert response.status_code == 404


@pytest.mark.test_endpoints
def test_put_InsertNewItem(client):
    item = {"_id": 999, "name": "Test object", "sell_in": 1099, "quality": 2000}
    response = client.put("/items/insert/", json=item)
    assert response.status_code == 201
    assert response.get_json() == {
        "Message": "The item has been introduced with id 999"
    }


@pytest.mark.test_endpoints
def test_put_UpdateAnExistingItem(client):
    item = {"_id": 999, "name": "Test object", "sell_in": 199, "quality": 2000}
    response = client.put("/items/insert/", json=item)
    assert response.status_code == 200


@pytest.mark.test_endpoints
def test_post_UpdateMethodOnNonExistingItem(client):
    response = client.post("/items/update/2132313")
    assert response.status_code == 404
    assert response.get_json() == {
        "Error Message": "The item with id 2132313 not exist"
    }


@pytest.mark.test_endpoints
def test_post_UpdateMethodOnExistingItem(client):
    response = client.post("/items/update/999")
    assert response.status_code == 200


@pytest.mark.test_endpoints
def test_put_InsertAnNonItem(client):
    response = client.put("/items/update/9ewwefwf")
    assert response.status_code == 404


@pytest.mark.test_endpoints
def test_delete_ExistingItem(client):
    response = client.delete("/items/delete/999")
    assert response.status_code == 202
    assert response.get_json() == {"Message": "The item has been deleted with id 999"}


@pytest.mark.test_endpoints
def test_delete_NotExistingItem(client):
    response = client.delete("/items/delete/999")
    assert response.status_code == 404
    assert response.get_json() == {"Message": "The item is not in the DB"}


@pytest.mark.test_endpoints
def test_get_GetAllItems(client):
    response = client.get("/items/all")
    assert response.status_code == 200


@pytest.mark.test_endpoints
def test_get_UpdateAllItems(client):
    response = client.get("/db/update")
    assert response.status_code == 200


@pytest.mark.test_endpoints
def test_get_DeleteDb(client):
    response = client.get("/db/drop")
    assert response.status_code == 200
