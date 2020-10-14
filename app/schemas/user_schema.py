from typing import List, Optional

from pydantic import BaseModel
from .item_schema import Item


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    username: str
    # email: Optional[str] = None
    full_name: Optional[str] = None
    disabled: Optional[bool] = None
    # is_active: bool
    items: List[Item] = []

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
