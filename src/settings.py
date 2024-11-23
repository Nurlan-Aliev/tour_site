from pydantic import BaseModel
from pydantic_settings import BaseSettings
from dotenv import load_dotenv
import os


load_dotenv()


class Settings(BaseModel):
    API_KEY: str = os.getenv("API_KEY")
    url: str = "http://api.weatherapi.com/v1"


settings = Settings()
print(settings.API_KEY)
