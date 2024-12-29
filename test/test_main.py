import pytest
from fastapi.testclient import TestClient
from src.main import app
from unittest.mock import MagicMock, patch


@pytest.fixture()
def client():
    return TestClient(app)


@pytest.mark.asyncio
async def test_home_page_cached_data(client, capsys):
    mock_redis = MagicMock()
    mock_redis.hgetall.side_effect = [
        {
            "name": "Baku",
            "temp_c": 9.1,
            "temp_f": 48.4,
            "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
            "text": "Sunny",
        },
        {
            "AZN": 1,
            "RUB": 61.2681,
            "USD": 0.5883,
            "EUR": 0.5604,
            "CNY": 4.284,
        },
    ]

    with patch("src.home_page.view.db_redis", mock_redis):
        response = client.get("/")
        content = response.text
        mock_redis.hgetall.assert_any_call("weather")
        mock_redis.hgetall.assert_any_call("currency")

        assert response.status_code == 200
        assert "9.1" in content
        assert "//cdn.weatherapi.com/weather/64x64/day/113.png" in content
        assert "61.2681" in content
        assert "0.5883" in content
