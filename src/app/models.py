from sqlmodel import SQLModel, Field
from typing import Optional

class AreaBase(SQLModel):
    name: str
    parent: Optional[int] = Field(default=None, foreign_key="area.id")

class Area(AreaBase, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)

class AreaCreate(AreaBase):
    pass