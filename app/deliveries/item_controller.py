from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import item_schema, general_schema
from app.usecases.item_service import ItemService
from app.middlewares import deps, di

router = APIRouter()
local_prefix = "/items/"


class ItemController():

    @router.post("/users/{user_id}"+local_prefix,
                 response_model=item_schema.Item)
    def create_item_for_user(
                user_id: str,
                item: item_schema.ItemCreate,
                db: Session = Depends(deps.get_db)
            ):
        return ItemService.create(db=db, item=item, user_id=user_id)

    @router.put(local_prefix+"{item_id}",
                response_model=item_schema.Item)
    def update_item(
                item_id: int,
                item: item_schema.ItemCreate,
                db: Session = Depends(deps.get_db)
            ):
        db_item = ItemService.read(db, item_id=item_id)
        if db_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return ItemService.update(db=db, item=item, item_id=item_id)

    @router.get(local_prefix,
                response_model=List[item_schema.Item])
    def read_items(
                commons: dict = Depends(di.common_parameters),
                db: Session = Depends(deps.get_db)
            ):
        items = ItemService.reads(
                db,
                skip=commons['skip'],
                limit=commons['limit']
            )
        return items

    @router.get(local_prefix+"{item_id}",
                response_model=item_schema.Item)
    def read_item(item_id: int, db: Session = Depends(deps.get_db)):
        db_item = ItemService.read(db, item_id=item_id)
        if db_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        return db_item

    @router.delete(local_prefix,
                   response_model=general_schema.Delete)
    def delete_item(
                item: item_schema.ItemId,
                db: Session = Depends(deps.get_db)
            ):
        db_item = ItemService.read(db, item_id=item.id)
        if db_item is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="Item not found")
        ItemService.delete(db=db, item_id=item.id)
        return {"id": item.id}
