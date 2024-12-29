from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from database.database import r as db_redis
from src.home_page.utils import cache_data

router = APIRouter(tags=["Home_Page"])
templates = Jinja2Templates(directory="src/home_page/templates")


@router.get("/")
async def home_page(request: Request):
    weather = db_redis.hgetall("weather")
    currency = db_redis.hgetall("currency")
    if not weather or not currency:
        weather, currency = await cache_data()

    return templates.TemplateResponse(
        request=request,
        name="index.html",
        context={"weather": weather, "currency": currency},
    )
