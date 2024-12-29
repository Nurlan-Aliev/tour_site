from settings import settings
from aiohttp import ClientSession


CITY = "Baku"


async def parse_weather(data: dict) -> dict:
    return {
        "name": data["location"]["name"],
        "temp_c": data["current"]["temp_c"],
        "temp_f": data["current"]["temp_f"],
        "icon": data["current"]["condition"]["icon"],
        "text": data["current"]["condition"]["text"],
    }


async def parse_currency(data: dict) -> dict:
    return {
        "AZN": data["conversion_rates"]["AZN"],
        "RUB": data["conversion_rates"]["RUB"],
        "USD": data["conversion_rates"]["USD"],
        "EUR": data["conversion_rates"]["EUR"],
        "CNY": data["conversion_rates"]["CNY"],
    }


async def get_api_data(session=ClientSession):
    async with session() as session:

        async with session.get(
            f"{settings.WEATHER_URL}/current.json",
            params={"key": settings.WEATHER_API_KEY, "q": CITY},
        ) as response:
            weather = await response.json()

        async with session.get(settings.currency_url) as response:
            currency = await response.json()
    return await parse_weather(weather), await parse_currency(currency)
