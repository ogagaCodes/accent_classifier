import pytest
from fastapi.testclient import TestClient
from index import app
@pytest.fixture(scope='module')
def client(): return TestClient(app)