from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from app.db.database import get_db
from app.models.task_model import Task
from app.schemas.task_schema import TaskCreate, TaskResponse

router = APIRouter()


@router.post("/tasks", response_model=TaskResponse)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):

    new_task = Task(
        title=task.title,
        description=task.description
    )

    db.add(new_task)

    db.commit()

    db.refresh(new_task)

    return new_task


@router.get("/tasks", response_model=list[TaskResponse])
def get_tasks(db: Session = Depends(get_db)):

    tasks = db.query(Task).all()

    return tasks