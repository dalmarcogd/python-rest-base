from starlette.testclient import TestClient

from src.app import app
from src.settings import BASE_PATH

client = TestClient(app)


def test_read_main():
    response = client.get(f"{BASE_PATH}/health-check")
    assert response.status_code == 200
    assert response.json() == {"status": "OK"}
