from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List
from app.schemas.task import Task, TaskCreate, TaskStatus
from app.crud.task import (
    get_tasks,
    get_user_tasks,
    get_task,
    create_user_task,
    update_task as update_task_crud,
    delete_task as delete_task_crud,
    mark_task_completed,
    get_tasks_by_status as get_tasks_by_status_crud
)
from app.database import get_db
from app.auth.auth import get_current_user
from app.models.user import User
from app.models.task import Task as TaskModel

router = APIRouter()

@router.get("/tasks/", response_model=List[Task])
def read_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tasks = get_user_tasks(db, user_id=current_user.id, skip=skip, limit=limit)
    return tasks

@router.get("/tasks/all", response_model=List[Task])
def read_all_tasks(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    if current_user.username != "admin":
        raise HTTPException(status_code=403, detail="Only admin can access all tasks")
    tasks = get_tasks(db, skip=skip, limit=limit)
    return tasks

@router.get("/tasks/{task_id}", response_model=Task)
def read_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.user_id != current_user.id and current_user.username != "admin":
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return db_task

@router.post("/tasks/", response_model=Task, status_code=status.HTTP_201_CREATED)
def create_task(
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    return create_user_task(db, task=task, user_id=current_user.id)

@router.put("/tasks/{task_id}", response_model=Task)
def update_task(
    task_id: int,
    task: TaskCreate,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return update_task_crud(db, db_task=db_task, task=task)

@router.delete("/tasks/{task_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    delete_task_crud(db, db_task=db_task)
    return None

@router.post("/tasks/{task_id}/complete", response_model=Task)
def complete_task(
    task_id: int,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    db_task = get_task(db, task_id=task_id)
    if db_task is None:
        raise HTTPException(status_code=404, detail="Task not found")
    if db_task.user_id != current_user.id:
        raise HTTPException(status_code=403, detail="Not enough permissions")
    return mark_task_completed(db, db_task=db_task)

@router.get("/tasks/status/{status}", response_model=List[Task])
def get_tasks_by_status_endpoint(
    status: TaskStatus,
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db),
    current_user: User = Depends(get_current_user)
):
    tasks = get_tasks_by_status_crud(db, status, skip, limit)
    # Filter only user's tasks unless admin
    if current_user.username != "admin":
        tasks = [task for task in tasks if task.user_id == current_user.id]
    return tasks