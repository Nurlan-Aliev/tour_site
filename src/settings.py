from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseModel):
    WEATHER_API_KEY: str = os.getenv("API_KEY")
    WEATER_URL: str = "http://api.weatherapi.com/v1"
    CURRENCY_API_KEY: str = os.getenv("CURENCY_API")
    CURRENCY_URL: str = (
        f"https://v6.exchangerate-api.com/v6/{CURRENCY_API_KEY}/latest/AZN"
    )


settings = Settings()
