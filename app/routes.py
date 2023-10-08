from http import HTTPStatus
from fastapi.params import Body
from fastapi import APIRouter, Request
from fastapi.logger import logger

from app.models import CreateMenu, UpdateMenu
from app.service import *
from app.utils import generate_response

router = APIRouter(prefix="/menu")

LOGGER_KEY = "app.router"


@router.get("/public/healthz")
async def health_check():
    return {"message": "OK"}


@router.post("/")
async def create_menu(body: CreateMenu = Body(...)):
    logger.info(f"{LOGGER_KEY}.create_menu")
    validated_data = body.dict()
    restaurant_id = validated_data.get("restaurant_id")
    item_name = validated_data.get("name")
    if await item_exists(item_name, restaurant_id):
        return {"status": False, "message": f"User already exists", "code": HTTPStatus.BAD_REQUEST.value}

    validated_data['restaurant_id'] = restaurant_id
    response = await add_item(validated_data)
    return await generate_response(**response)


@router.get("/")
async def get_menu(request: Request):
    logger.info(f"{LOGGER_KEY}.get_user")
    params = dict(request.query_params)
    response = await get_menu_items(params)
    return await generate_response(**response)


@router.get("/item")
async def get_item(request: Request):
    logger.info(f"{LOGGER_KEY}.get_item")
    params = dict(request.query_params)
    response = await get_item_from_all_restaurants(params)
    return await generate_response(**response)


@router.patch("/")
async def update_menu(body: UpdateMenu = Body(...)):
    logger.info(f"{LOGGER_KEY}.update_menu")
    response = await update_menu_items(body.dict())
    return await generate_response(**response)