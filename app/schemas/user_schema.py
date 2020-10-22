from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str
    full_name: Optional[str] = None


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: str
    is_active: Optional[bool] = 1

    class Config:
        orm_mode = True


class UserId(BaseModel):
    id: str


class UserInDB(User):
    hashed_password: str
