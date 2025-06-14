from fastapi.testclient import TestClient
from http import HTTPStatus
from fastapi_new.app import app

client = TestClient(app)


def test_read_root():
    response = client.get('/')
    assert response.status_code == HTTPStatus.OK
    assert response.json() == {'Message': 'Hello World'}
