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


def get_users(db: Session,
              skip: int = 0,
              limit: int = 100,
              active: bool = True):
    return db.query(
        user_model.User
    ).filter(
        user_model.User.is_active == active
    ).offset(skip).limit(limit).all()


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


def update_user(db: Session, user: user_schema.UserCreate, user_id: str):
    hashpass = create_hashing(user.password)
    db.query(
        user_model.User
    ).filter(
        user_model.User.id == user_id
    ).update({
        user_model.User.full_name: user.full_name,
        user_model.User.email: user.email,
        user_model.User.hashed_password: hashpass,
    })
    db.commit()
    return db.query(
        user_model.User
    ).filter(user_model.User.id == user_id).first()


def delete_user(db: Session, user_id: str):
    db_user = db.query(
        user_model.User
    ).filter(user_model.User.id == user_id).first()
    # use this one for hard delete:
    # db.delete(db_user)
    # use this one for soft delete (is_active)
    db.query(
        user_model.User
    ).filter(
        user_model.User.id == user_id
    ).update({
        user_model.User.is_active: 0,
    })

    db.commit()
    return db_user
