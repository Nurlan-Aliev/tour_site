from src.api_clients import parse_currency, parse_weather, get_api_data
import asyncio


class MyClientSession:
    def __init__(self):
        data = [
            {
                "location": {
                    "name": "Baku",
                },
                "current": {
                    "temp_c": 9.1,
                    "temp_f": 48.4,
                    "condition": {
                        "text": "Sunny",
                        "icon": "//cdn.weatherapi.com/weather/64x64/day/113.png",
                        "code": 1000,
                    },
                },
            },
            {
                "conversion_rates": {
                    "AZN": 1,
                    "AED": 2.1604,
                    "BOB": 4.0738,
                    "CLP": 577.476,
                    "CNY": 4.284,
                    "ERN": 8.8239,
                    "ETB": 74.681,
                    "EUR": 0.5604,
                    "LAK": 12915.6868,
                    "RUB": 61.2681,
                    "SHP": 0.4658,
                    "USD": 0.5883,
                },
            },
        ]
        self.data = iter(data)

    def get(self, *args, **kwargs):
        return self

    async def json(self):
        return self.data.__next__()

    async def __aenter__(self):
        return self

    async def __aexit__(self, exc_type, exc_val, exc_tb):
        return False


def test_get_api_data():
    assert asyncio.run(get_api_data(MyClientSession)) == (
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
    )
