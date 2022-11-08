from fastapi import Depends
from sqlmodel import Session
from config.db import get_session
from config.main import app
from app.models import Area, AreaCreate

@app.get("/ping")
def pong():
    return {"ping": "pong!"}

@app.post("/area/", response_model=Area)
def create_area(area: AreaCreate, session: Session = Depends(get_session)):
    item = Area.from_orm(area)
    session.add(item)
    session.commit()
    session.refresh(item)
    return item