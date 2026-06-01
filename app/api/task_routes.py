from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.task_model import Task
from app.models.user_model import User
from app.schemas.task_schema import TaskCreate, TaskResponse
from app.dependencies.auth import get_current_user

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create_task(
    task: TaskCreate,
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):

    new_task = Task(
        title=task.title,
        description=task.description,
        owner_id=current_user.id
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task


@router.get("/tasks")
def get_tasks(
    current_user: User = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    return db.query(Task).filter(Task.owner_id == current_user.id).all()