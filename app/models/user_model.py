from sqlalchemy import Boolean, Column, String
from sqlalchemy.orm import relationship

from config.database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(String(50), primary_key=True, index=True)
    email = Column(String(100), unique=True, index=True)
    full_name = Column(String(100))
    hashed_password = Column(String(100))
    is_active = Column(Boolean, default=True)

    items = relationship("Item", back_populates="owner")
