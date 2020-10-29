from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import RepositoryInterface
from app.models import item_model
from app.schemas import item_schema


class ItemRepository(RepositoryInterface):

    def reads(db: Session, skip: int = 0, limit: int = 100):
        return db.query(
            item_model.Item
        ).offset(skip).limit(limit).all()

    def read(db: Session, item_id: int):
        return db.query(
            item_model.Item
        ).filter(item_model.Item.id == item_id).first()

    def create(
            db: Session,
            item: item_schema.ItemCreate,
            user_id: str):
        db_item = item_model.Item(**item.dict(), owner_id=user_id)
        db.add(db_item)
        db.commit()
        db.refresh(db_item)
        return db_item

    def update(db: Session, item: item_schema.ItemCreate, item_id: int):
        db.query(
            item_model.Item
        ).filter(
            item_model.Item.id == item_id
        ).update({
            item_model.Item.title: item.title,
            item_model.Item.description: item.description,
        })

        db.commit()
        return db.query(
            item_model.Item
        ).filter(item_model.Item.id == item_id).first()

    def delete(db: Session, item_id: int):
        # use this one for hard delete:
        db.query(
            item_model.Item
        ).filter(item_model.Item.id == item_id).delete()
        db.commit()
        return True
