from sqlalchemy import Boolean, Column, Integer, String
from sqlalchemy.orm import relationship
# from sqlalchemy_utils import UUIDType
# from uuid import UUID

from config.database import Base
# from app.utils.uuid import generate_uuid


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    # id = Column(String(100), primary_key=True, index=True)
    # id = Column(String(100), primary_key=True, default=UUID, index=True)
    # id = Column(UUIDType(binary=False), primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    full_name: Column(String(100), unique=True, index=True)
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
