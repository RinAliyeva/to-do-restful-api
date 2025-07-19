from sqlalchemy import Column, Integer, String, Text
from sqlalchemy.orm import relationship
from .task import Task
from app.database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    first_name = Column(String(50), nullable=False)
    last_name = Column(Text, nullable=True)
    username = Column(String(50), unique=True, index=True, nullable=False)
    password = Column(String(100), nullable=False)

    tasks = relationship("Task", back_populates="owner")