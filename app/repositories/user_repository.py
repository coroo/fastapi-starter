from sqlalchemy.orm import Session

from app.models import user_model
from app.schemas import user_schema
from app.utils.hash import create_hashing
from app.utils.uuid import generate_uuid


def get_user(db: Session, user_id: int):
    return db.query(
        user_model.User
    ).filter(user_model.User.id == user_id).first()


def get_user_by_email(db: Session, email: str):
    return db.query(
        user_model.User
    ).filter(user_model.User.email == email).first()


def get_users(db: Session, skip: int = 0, limit: int = 100):
    return db.query(user_model.User).offset(skip).limit(limit).all()


def create_user(db: Session, user: user_schema.UserCreate):
    uuid = generate_uuid()
    hashpass = create_hashing(user.password)
    db_user = user_model.User(
        id=uuid,
        full_name=user.full_name,
        email=user.email,
        hashed_password=hashpass)
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user
