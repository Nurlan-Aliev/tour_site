from pydantic_settings import BaseSettings, SettingsConfigDict
from dotenv import load_dotenv


load_dotenv()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_file=".env")
    RE_HOST: str
    RE_PORT: int
    RE_USERNAME: str
    RE_PASS: str

    DB_NAME: str
    DB_PASS: str
    DB_USER: str
    DB_PORT: int
    DB_HOST: str

    WEATHER_API_KEY: str
    CURRENCY_API_KEY: str

    WEATHER_URL: str = "http://api.weatherapi.com/v1"

    @property
    def currency_url(self) -> str:
        return f"https://v6.exchangerate-api.com/v6/{self.CURRENCY_API_KEY}/latest/AZN"

    @property
    def db_connect(self):
        return f"postgresql+asyncpg://{self.DB_USER}:{self.DB_PASS}@{self.DB_HOST}:{self.DB_PORT}/{self.DB_NAME}"


settings = Settings()
