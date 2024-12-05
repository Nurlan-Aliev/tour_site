from src.settings import settings
import aiohttp
import asyncio


async def get_api_data():
    async with aiohttp.ClientSession() as session:

        async with session.get(
            f"{settings.WEATER_URL}/current.json",
            params={"key": settings.WEATHER_API_KEY, "q": "Baku"},
        ) as response:
            weather = await response.json()

        async with session.get(f"{settings.CURRENCY_URL}") as response:
            currency = await response.json()

    return weather, currency


async def my_async_function():
    while True:
        await get_api_data()
        await asyncio.sleep(60)
