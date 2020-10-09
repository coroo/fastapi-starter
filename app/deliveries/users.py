from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from sqlalchemy.orm import Session
from app.schemas import user_schema
from app.usecases import user_usecase
from app.middlewares import deps, di
from datetime import datetime

import logging
logging.basicConfig(filename='logs/{:%Y-%m-%d}.log'.format(datetime.now()), level=logging.DEBUG,
                    format='%(asctime)s:%(levelname)s - %(message)s')

router = APIRouter()
local_prefix = "/users/"


@router.post(local_prefix, response_model=user_schema.User)
def create_user(user: user_schema.UserCreate, db: Session = Depends(deps.get_db)):
    db_user = user_usecase.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST, detail="Email already registered")
    return user_usecase.create_user(db=db, user=user)


@router.get(local_prefix, response_model=List[user_schema.User])
def read_users(commons: dict = Depends(di.common_parameters), db: Session = Depends(deps.get_db)):
    users = user_usecase.get_users(db, skip=commons['skip'], limit=commons['limit'])
    return users


@router.get(local_prefix+"{user_id}", response_model=user_schema.User)
def read_user(user_id: int, db: Session = Depends(deps.get_db)):
    db_user = user_usecase.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user
