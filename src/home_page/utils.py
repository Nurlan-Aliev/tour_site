from src.settings import settings
import aiohttp
import asyncio
from src.database.config import r as db_redis

CITY = "Baku"


async def get_api_data():
    async with aiohttp.ClientSession() as session:

        async with session.get(
            f"{settings.WEATER_URL}/current.json",
            params={"key": settings.WEATHER_API_KEY, "q": CITY},
        ) as response:
            weather = await response.json()

        async with session.get(f"{settings.CURRENCY_URL}") as response:
            currency = await response.json()

    return weather, currency


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


async def cache_data():
    weather, currency = await get_api_data()
    weather = await parse_weather(weather)
    currency = await parse_currency(currency)
    db_redis.hset("weather", mapping=weather)
    db_redis.expire("weather", 21_600)

    db_redis.hset("currency", mapping=currency)
    db_redis.expire("db_redis", 21_600)
    return weather, currency
