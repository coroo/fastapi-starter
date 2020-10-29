from sqlalchemy.orm import Session

from app.interfaces.api_interfaces import ServiceInterface
from app.repositories.user_repository import UserRepository
from app.schemas import user_schema


class UserService(ServiceInterface):

    def read(db: Session, user_id: int):
        return UserRepository.read(db, user_id=user_id)

    def read_by_email(db: Session, email: str):
        return UserRepository.read_by_email(db, email=email)

    def reads(db: Session,
              skip: int = 0,
              limit: int = 100,
              active: bool = True):
        return UserRepository.reads(
            db,
            skip=skip,
            limit=limit,
            active=active)

    def create(db: Session, user: user_schema.UserCreate):
        return UserRepository.create(db=db, user=user)

    def update(db: Session, user: user_schema.UserCreate, user_id: str):
        return UserRepository.update(db=db, user=user, user_id=user_id)

    def delete(db: Session, user_id: str):
        return UserRepository.delete(db=db, user_id=user_id)
