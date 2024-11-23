from fastapi import FastAPI
from src.home_page.view import router as home_page_router


app = FastAPI()

app.include_router(home_page_router)
