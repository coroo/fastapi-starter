from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.item_repository import ItemRepository
from app.schemas import item_schema


class ItemService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return ItemRepository.reads(db, skip=skip, limit=limit)

    def read(db: Session, item_id: int):
        return ItemRepository.read(db, item_id=item_id)

    def create(db: Session,
               item: item_schema.ItemCreate,
               user_id: int):
        return ItemRepository.create(
            db=db,
            item=item,
            user_id=user_id)

    def update(db: Session, item: item_schema.ItemCreate, item_id: int):
        return ItemRepository.update(db=db, item=item, item_id=item_id)

    def delete(db: Session, item_id: str):
        return ItemRepository.delete(db=db, item_id=item_id)
