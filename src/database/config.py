from redis import Redis
from dotenv import load_dotenv
import os

load_dotenv()

r = Redis(
    host=os.getenv("REHOST"),
    port=os.getenv("REPORT"),
    password=os.getenv("REPASS"),
    decode_responses=True,
)
