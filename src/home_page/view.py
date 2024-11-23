from fastapi import APIRouter, Request
from fastapi.templating import Jinja2Templates
from src.settings import settings
import aiohttp

router = APIRouter(tags={"Home Page"})
templates = Jinja2Templates(directory="src/home_page/templates")


@router.get("/")
async def home_page(request: Request):
    async with aiohttp.ClientSession as session:
        async with session.get(
            f"{settings.url}/current.json",
            params={"key": settings.API_KEY, "q": "Baku"},
        ) as response:
            weather = await response.json()
    return templates.TemplateResponse(
        request, "index.html", context={"weather": weather}
    )
