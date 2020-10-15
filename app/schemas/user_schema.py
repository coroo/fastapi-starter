from typing import Optional

from pydantic import BaseModel


class UserBase(BaseModel):
    email: str


class UserCreate(UserBase):
    password: str


class User(UserBase):
    id: int
    # username: str
    email: str
    # email: Optional[str] = None
    full_name: Optional[str] = None
    is_active: Optional[bool] = None
    # is_active: bool

    class Config:
        orm_mode = True


class UserInDB(User):
    hashed_password: str
