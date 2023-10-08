from typing import Optional
from pydantic import BaseModel, Extra
from pydantic.class_validators import validator
from pydantic.fields import Field

from app.constants import email_regex, phone_regex, Roles, Address


class MenuBaseModel(BaseModel):
    class Config:
        use_enum_values = True  # Uses Enum Values
        extra = Extra.ignore  # Ignores Extra Values
        str_strip_whitespace = True  # Removes Whitespaces


class CreateMenu(MenuBaseModel):
    restaurant_id: str = Field(...)
    name: str = Field(...)
    description: Optional[str] = None
    price: float = Field(None)
    stock_quantity: int = 0
    is_available: bool = False

class UpdateMenu(MenuBaseModel):
    item_id: str = Field(...)
    restaurant_id: str = Field(...)
    name: Optional[str] = Field(...)
    description: Optional[str] = None
    price: float = Field(None)
    stock_quantity: int = 0
    is_available: bool = False
