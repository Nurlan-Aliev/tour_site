from database.config import r as db_redis
from src.api_clients import get_api_data


async def cache_data():
    weather, currency = await get_api_data()
    db_redis.hset("weather", mapping=weather)
    db_redis.expire("weather", 21_600)

    db_redis.hset("currency", mapping=currency)
    db_redis.expire("db_redis", 21_600)
    return weather, currency
