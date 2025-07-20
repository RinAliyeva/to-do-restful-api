from sqlalchemy.orm import Session
from app.models.task import Task as TaskModel, TaskStatus
from app.schemas.task import TaskCreate

def get_tasks(db: Session, skip: int = 0, limit: int = 100):
    return db.query(TaskModel).offset(skip).limit(limit).all()

def get_user_tasks(db: Session, user_id: int, skip: int = 0, limit: int = 100):
    return db.query(TaskModel).filter(TaskModel.user_id == user_id).offset(skip).limit(limit).all()

def get_task(db: Session, task_id: int):
    return db.query(TaskModel).filter(TaskModel.id == task_id).first()

def create_user_task(db: Session, task: TaskCreate, user_id: int):
    db_task = TaskModel(**task.model_dump(), user_id=user_id)
    db.add(db_task)
    db.commit()
    db.refresh(db_task)
    return db_task

def update_task(db: Session, db_task: TaskModel, task: TaskCreate):
    for field, value in task.model_dump().items():
        setattr(db_task, field, value)
    db.commit()
    db.refresh(db_task)
    return db_task

def delete_task(db: Session, db_task: TaskModel):
    db.delete(db_task)
    db.commit()

def mark_task_completed(db: Session, db_task: TaskModel):
    db_task.status = TaskStatus.COMPLETED
    db.commit()
    db.refresh(db_task)
    return db_task

def get_tasks_by_status(db: Session, status: TaskStatus, skip: int = 0, limit: int = 100):
    return db.query(TaskModel).filter(TaskModel.status == status).offset(skip).limit(limit).all()
