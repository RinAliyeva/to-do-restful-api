from pydantic import BaseModel, ConfigDict
from typing import Optional
from enum import Enum

class TaskStatus(str, Enum):
    NEW = "New"
    IN_PROGRESS = "In Progress"
    COMPLETED = "Completed"

class TaskBase(BaseModel):
    title: str
    description: Optional[str] = None
    status: Optional[TaskStatus] = TaskStatus.NEW

class TaskCreate(TaskBase):
    pass

class Task(TaskBase):
    id: int
    user_id: int

    model_config = ConfigDict(from_attributes=True)