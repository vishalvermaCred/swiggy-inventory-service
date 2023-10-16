from typing import Optional
from pydantic import BaseModel, Extra
from pydantic.fields import Field

"""
    creating models to validate the payload of APIs using pydantic
"""


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
    restaurant_id: Optional[str] = None
    name: Optional[str] = None
    description: Optional[str] = None
    price: float = Field(None)
    ordered_quantity: int = 0
    restock_quantity: int = 0
    is_available: bool = False
