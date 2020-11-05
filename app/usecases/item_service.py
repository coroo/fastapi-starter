from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.item_repository import ItemRepository as repository
from app.schemas import item_schema as schema


class ItemService(ServiceInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return repository.reads(db, skip=skip, limit=limit)

    def read(db: Session, item_id: int):
        return repository.read(db, item_id=item_id)

    def create(db: Session,
               item: schema.ItemCreate,
               user_id: int):
        return repository.create(
            db=db,
            item=item,
            user_id=user_id)

    def update(db: Session, item: schema.ItemCreate, item_id: int):
        return repository.update(db=db, item=item, item_id=item_id)

    def delete(db: Session, item_id: str):
        return repository.delete(db=db, item_id=item_id)
