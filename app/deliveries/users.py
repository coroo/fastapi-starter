from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from app.schemas import user_schema, token_schema
from app.usecases import user_usecase
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/users/"


@router.post("/token", response_model=token_schema.Token)
async def login(
        form_data: OAuth2PasswordRequestForm = Depends(),
        db: Session = Depends(deps.get_db)
        ):
    user = auth.authenticate_user(db, form_data.username, form_data.password)
    if not user:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Bearer"},
        )
    access_token_expires = timedelta(minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = auth.create_access_token(
        data={"sub": user.email}, expires_delta=access_token_expires
    )
    return {"access_token": access_token, "token_type": "bearer"}


@router.get("/users/me/", response_model=user_schema.User)
async def read_users_me(
        current_user: user_schema.User = Depends(
            auth.get_current_active_user)
        ):
    return current_user


@router.post(local_prefix, response_model=user_schema.User)
def create_user(
        user: user_schema.UserCreate,
        db: Session = Depends(deps.get_db)
        ):
    db_user = user_usecase.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered")
    return user_usecase.create_user(db=db, user=user)


@router.get(local_prefix, response_model=List[user_schema.User])
def read_users(
        commons: dict = Depends(di.common_parameters),
        db: Session = Depends(deps.get_db)
        ):
    users = user_usecase.get_users(
        db, skip=commons['skip'], limit=commons['limit'])
    return users


@router.get(local_prefix+"{user_id}", response_model=user_schema.User)
def read_user(
            user_id: int,
            db: Session = Depends(deps.get_db),
            current_user: user_schema.User = Depends(
                auth.get_current_active_user
            )
        ):
    db_user = user_usecase.get_user(db, user_id=user_id)
    if db_user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
    return db_user
