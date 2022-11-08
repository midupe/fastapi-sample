from fastapi import Depends
from sqlmodel import Session
from config.db import get_session
from config.main import app
from app.models import Task, TaskCreate

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.post("/task/", response_model=Task)
def create_task(task: TaskCreate, session: Session = Depends(get_session)):
    db_task = Task.from_orm(task)
    session.add(db_task)
    session.commit()
    session.refresh(db_task)
    return db_task