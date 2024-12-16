import pytest
from fastapi.testclient import TestClient
from src.main import app
import re


@pytest.fixture()
def client():
    return TestClient(app)


# def test_something(capsys):
#     with capsys.disabled():
#         print(response.headers)


def test_read_item(client):
    response = client.get("/")
    content = response.text
    assert response.status_code == 200
    assert "text/html" in response.headers["Content-Type"]
    re.search(r"<[^>]+>", content)
