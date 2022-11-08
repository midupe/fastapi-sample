#start app
from fastapi import FastAPI
from config.db import create_db_and_tables

app = FastAPI()

"""
#auto generate database tables
@app.on_event("startup")
def on_startup():
    create_db_and_tables()
"""

from app.views import *
    