from sqlalchemy import Boolean, Column, ForeignKey, Integer, String
from sqlalchemy.dialects.postgresql import UUID
from sqlalchemy.orm import relationship

from .database import Base


class User(Base):
    __tablename__ = "users"

    id = Column(UUID, primary_key=True, index=True, server_default=text("uuid_generate_v4()"), primary_key=True)
    email = Column(String, unique=True, index=True)
    tel = Column(String, unique=True, index=True)
    password = Column(String)
    is_active = Column(Boolean, default=False)
    is_admin = Column(Boolean, default=False)
    is_coach = Column(Boolean, default=False)
    is_customer = Column(Boolean, default=False)
