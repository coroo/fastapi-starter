from sqlalchemy.orm import Session
from app.repositories import item_repository
from app.schemas import item_schema


def get_items(db: Session, skip: int = 0, limit: int = 100):
    return item_repository.get_items(db, skip=skip, limit=limit)


def get_item(db: Session, item_id: int):
    return item_repository.get_item(db, item_id=item_id)


def create_user_item(db: Session, item: item_schema.ItemCreate, user_id: int):
    return item_repository.create_user_item(db=db, item=item, user_id=user_id)
