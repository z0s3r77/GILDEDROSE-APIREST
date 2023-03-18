import pytest
from controller.main import app


# https://flask.palletsprojects.com/en/2.2.x/testing/
@pytest.fixture()
def application():
    test_app = app
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
