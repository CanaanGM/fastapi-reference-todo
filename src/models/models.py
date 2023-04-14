from datetime import datetime
from typing import Optional
from sqlalchemy import Boolean, Column, DateTime, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from ..Data.database import Base
from pydantic import BaseModel, Field

class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)
    description = Column(String)
    priority = Column(Integer)
    complete = Column(Boolean, default=False)
    date_added = Column(DateTime, default=datetime.utcnow())
    date_completed = Column(DateTime)

    owner_id = Column(Integer, ForeignKey("users.id"))
    owner = relationship("Users", back_populates="todos")

class TodoDto(BaseModel):
    title: str
    description: Optional[str]
    priority : int = Field(gt=0, lt=6, description="Between 1 - 5")
    complete: bool



class Users(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    email = Column(String, unique=True, index=True)
    username = Column(String, unique=True, index=True)
    first_name= Column(String)
    last_name= Column(String)
    hashed_password = Column(String)
    is_active = Column(Boolean, default=True)

    todos = relationship("Todo", back_populates="owner")

class UserDto(BaseModel):
    username: str
    email: str
    first_name: str
    last_name: str
    password: str
