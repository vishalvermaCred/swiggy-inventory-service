from enum import Enum

PSQL_USER_DB = "user_db"
phone_regex = r"^(0\d{10}|[1-9]\d{9,11})$"
email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"


class ResponseKeys:
    DATA = "data"
    SUCCESS = "success"
    MESSAGE = "message"
    ERROR = "error"


class Tables(Enum):
    MENU = {"name": "menu_items", "columns": ["item_id", "restaurant_id", "name", "description", "price", "stock_quantity", "is_available"]}


class Roles(Enum):
    ADMIN = "admin"
    CUSTOMER = "customer"
    RESTATURANT = "restaurant"
    DELIVERY_PERSONNEL = "delivery_personnel"
