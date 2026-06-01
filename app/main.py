from pathlib import Path

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles

from app.api.auth_routes import router as auth_router
from app.api.task_routes import router as task_router
from app.db.database import engine, Base

from app.models.task_model import Task
from app.models.user_model import User

Base.metadata.create_all(bind=engine)

app = FastAPI()

# Serve static files
STATIC_DIR = Path(__file__).resolve().parent / "static"
app.mount("/static", StaticFiles(directory=STATIC_DIR), name="static")


@app.get("/", response_class=HTMLResponse)
def root():
    index_file = STATIC_DIR / "index.html"
    return index_file.read_text(encoding="utf-8")


app.include_router(task_router)
app.include_router(auth_router)