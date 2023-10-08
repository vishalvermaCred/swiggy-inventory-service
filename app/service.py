from uuid import uuid4
from http import HTTPStatus
from fastapi.logger import logger

from app.context import app_context
from app.constants import Tables, Roles

LOGGER_KEY = "app.service"


async def item_exists(item_name, restaurant_id):
    logger.info(f"{LOGGER_KEY}.item_exists")
    select_query = f"select item_id from {Tables.MENU.value['name']} where name = '{item_name}' and restaurant_id = '{restaurant_id}';"
    item_data = await app_context.db.execute_raw_select_query(select_query)
    if item_data:
        return True
    return False


async def add_item(kwargs):
    logger.info(f"{LOGGER_KEY}.add_item")
    try:
        item_id = uuid4().hex
        user_columns = ", ".join(Tables.MENU.value["columns"])
        insert_user_query = f"INSERT INTO {Tables.MENU.value['name']} ({user_columns}) VALUES ('{item_id}', '{kwargs.get('fullname')}', '{kwargs.get('password_hash')}', '{kwargs.get('email')}', '{kwargs.get('phone_number')}', '{kwargs.get('role')}');"
        insert_response = await app_context.db.execute_insert_or_update_query(insert_user_query)
        logger.info(f"insert_response: {insert_response}")
        logger.info(f"{LOGGER_KEY}.add_item.item_id: {item_id}")
        return {"success": True, "message": "User created successfully", "code": HTTPStatus.OK.value}
    except Exception as e:
        logger.error(f"{LOGGER_KEY}.add_item.exceptiopn: {str(e)}")
        return {"success": False, "message": str(e), "code": HTTPStatus.INTERNAL_SERVER_ERROR.value}


async def get_menu_items(kwargs):
    logger.info(f"{LOGGER_KEY}.get_menu_items")
    try:
        restaurant_id = kwargs.get("restaurant_id")
        select_query = f"SELECT item_id, restaurant_id, name, description, price, stock_quantity, is_available FROM {Tables.MENU.value['name']} WHERE restaurant_id = '{restaurant_id}' and is_available=true;"
        menu_items = await app_context.db.execute_raw_select_query(select_query)
        if not menu_items:
            return {
                "success": False,
                "message": "Menu for given restaurant is not available",
                "code": HTTPStatus.BAD_REQUEST.value
            }
        return {
            "success": True,
            "message": "Menu fetched successfully",
            "code": HTTPStatus.OK.value,
            "data": menu_items
        }
    except Exception as e:
        logger.error(f"{LOGGER_KEY}.get_menu_items.exceptiopn: {str(e)}")
        return {"success": False, "message": str(e), "code": HTTPStatus.INTERNAL_SERVER_ERROR.value}


async def get_item_from_all_restaurants(kwargs):
    logger.info(f'{LOGGER_KEY}.get_item_from_all_restaurants')
    try:
        name = kwargs.get("name")
        select_query = f"SELECT item_id, restaurant_id, name, description, price, stock_quantity, is_available FROM {Tables.MENU.value['name']} WHERE name like %{name}%; and is_available = true"
        item_data = await app_context.db.execute_raw_select_query(select_query)
        if not item_data:
            return {
                "success": False,
                "message": "This item is not present right now",
                "code": HTTPStatus.BAD_REQUEST.value
            }
        return {
            "success": True,
            "message": "Menu fetched successfully",
            "code": HTTPStatus.OK.value,
            "data": item_data
        }
    except Exception as e:
        logger.error(f"{LOGGER_KEY}.get_item_from_all_restaurants.exceptiopn: {str(e)}")
        return {"success": False, "message": str(e), "code": HTTPStatus.INTERNAL_SERVER_ERROR.value}


async def update_menu_items(kwargs):
    logger.info(f"{LOGGER_KEY}.update_menu_items")
    try:
        item_id = kwargs.get("item_id")
        update_query = f"UPDATE {Tables.MENU.value['name']} SET "
        if kwargs.get('name'):
            update_query += f"name = '{kwargs.get('name')}', "
        if kwargs.get('description'):
            update_query += f"description = '{kwargs.get('description')}', "
        if kwargs.get('price'):
            update_query += f"price = '{kwargs.get('price')}', "
        if kwargs.get('stock_quantity'):
            update_query += f"stock_quantity = 'stock_quantity-{kwargs.get('stock_quantity')}', is_available = (stock_quantity-{kwargs.get('stock_quantity')})>0, "
        
        update_query = update_query.strip(", ")
        update_query += f" WHERE item_id = '{item_id}';"
        update_response = await app_context.db.execute_insert_or_update_query(update_query)
        logger.info(f"{LOGGER_KEY}.update_menu_items.update_response: {update_response}")
        return {
            "success": True,
            "message": "Menu item updated successfully",
            "code": HTTPStatus.OK.value,
        }
    except Exception as e:
        logger.error(f"{LOGGER_KEY}.update_menu_items.exceptiopn: {str(e)}")
        return {"success": False, "message": str(e), "code": HTTPStatus.INTERNAL_SERVER_ERROR.value}