from fastapi import APIRouter, Depends
from app.deliveries import (
        item_controller,
        user_controller,
    )
from app.middlewares import auth

api = APIRouter()


api.include_router(
    user_controller.router,
    tags=["users"])
api.include_router(
    item_controller.router,
    tags=["items"],
    dependencies=[Depends(auth.get_current_active_user)],
    responses={404: {"description": "Not found"}},
)
