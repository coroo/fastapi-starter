from sqlalchemy.orm import Session

from app.repositories import user_repository
from app.schemas import user_schema


def get_user(db: Session, user_id: int):
    return user_repository.get_user(db, user_id=user_id)


def get_user_by_email(db: Session, email: str):
    print("SAYA DI USECASE")
    test = user_repository.get_user_by_email(db, email=email)
    print("DI USECASE SETELAH CASE")
    return test
    # return user_repository.get_user_by_email(db, email=email)


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return user_repository.get_users(db, skip=skip, limit=limit)


def create_user(db: Session, user: user_schema.UserCreate):
    return user_repository.create_user(db=db, user=user)