from fastapi import FastAPI

from app.api.auth_routes import router as auth_router
from app.api.task_routes import router as task_router
from app.db.database import engine, Base

from app.models.task_model import Task
from app.models.user_model import User

Base.metadata.create_all(bind=engine)

app = FastAPI()


@app.get("/")
def root():
    return {"message": "TaskFlow API is running"}


app.include_router(task_router)
app.include_router(auth_router)