from sqlmodel import SQLModel, Field
from typing import Optional

class TaskBase(SQLModel):
    task_name: str
    task_description: Optional[str] = None

class Task(TaskBase, table=True):
    id: int = Field(default=None, primary_key=True)

class TaskCreate(TaskBase):
    pass

class Hero(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    name: str
    secret_name: str
    age: Optional[int] = None