from os import getenv

from dotenv import find_dotenv, load_dotenv

load_dotenv(find_dotenv())

ENV = getenv("ENV", "")
SERVICE_NAME = getenv("SERVICE_NAME", "")
APP_NAME = getenv("APP_NAME", "User Service")

BASE_ROUTE = getenv("BASE_ROUTE")
LOG_LEVEL = getenv("LOG_LEVEL", "INFO")

INVENTORY_DB_CONFIGS = {
    "HOST": getenv("DB_HOST"),
    "PORT": getenv("DB_PORT"),
    "NAME": getenv(f"INVENTORY_DB_NAME"),
    "PASSWORD": getenv("INVENTORY_DB_PASSWORD"),
    "USER": getenv("INVENTORY_DB_USER"),
}
