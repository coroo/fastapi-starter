from fastapi import Depends, APIRouter, HTTPException, status
from typing import List
from datetime import timedelta
from fastapi.security import OAuth2PasswordRequestForm

from sqlalchemy.orm import Session
from app.schemas import user_schema, token_schema
from app.usecases.user_service import UserService as usecase
from app.middlewares import deps, di, auth

router = APIRouter()
local_prefix = "/users/"


class UserController():

    @router.post(local_prefix+"token", response_model=token_schema.Token)
    async def login(
                form_data: OAuth2PasswordRequestForm = Depends(),
                db: Session = Depends(deps.get_db)
            ):
        user = auth.authenticate_user(
                db,
                form_data.username,
                form_data.password)
        if not user:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="Incorrect username or password",
                headers={"WWW-Authenticate": "Bearer"},
            )
        access_token_expires = timedelta(
            minutes=auth.ACCESS_TOKEN_EXPIRE_MINUTES)
        access_token = auth.create_access_token(
            data={"sub": user.email}, expires_delta=access_token_expires
        )
        return {"access_token": access_token,
                "user_key": user.id,
                "token_type": "bearer"}

    @router.get(local_prefix+"me/", response_model=user_schema.User)
    async def read_users_me(
            current_user: user_schema.User = Depends(
                auth.get_current_active_user)
            ):
        return current_user

    @router.post(local_prefix, response_model=user_schema.User)
    def create_user(
            user: user_schema.UserCreate,
            db: Session = Depends(deps.get_db),
            current_user: user_schema.User = Depends(
                auth.get_current_active_user)
            ):
        db_user = usecase.read_by_email(db, email=user.email)
        if db_user:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Email already registered")
        return usecase.create(db=db, user=user)

    @router.put(local_prefix+"{user_id}", response_model=user_schema.User)
    def update_user(
                user_id: str,
                user: user_schema.UserCreate,
                db: Session = Depends(deps.get_db)
            ):
        db_user = usecase.read(db, user_id=user_id)
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return usecase.update(db=db, user=user, user_id=user_id)

    @router.get(local_prefix, response_model=List[user_schema.User])
    def read_users(
            commons: dict = Depends(di.common_parameters),
            active: bool = True,
            db: Session = Depends(deps.get_db),
            current_user: user_schema.User = Depends(
                auth.get_current_active_user)
            ):
        users = usecase.reads(
            db, skip=commons['skip'], limit=commons['limit'], active=active)
        return users

    @router.get(local_prefix+"{user_id}", response_model=user_schema.User)
    def read_user(
                user_id: str,
                db: Session = Depends(deps.get_db),
                current_user: user_schema.User = Depends(
                    auth.get_current_active_user)
            ):
        db_user = usecase.read(db, user_id=user_id)
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return db_user

    @router.delete(local_prefix, response_model=user_schema.User)
    def delete_user(
                user: user_schema.UserId,
                db: Session = Depends(deps.get_db)
            ):
        db_user = usecase.read(db, user_id=user.id)
        if db_user is None:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND, detail="User not found")
        return usecase.delete(db=db, user_id=user.id)
