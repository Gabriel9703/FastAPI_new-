import pytest
from fastapi.testclient import TestClient

from fastapi_new.app import app


@pytest.fixture
def client():
    return TestClient(app)
