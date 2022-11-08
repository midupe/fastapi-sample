from main import app
from config.settings import sql

@app.get("/v1/animals")
async def animals():
    return sql("SELECT * FROM animals")

@app.get("/v1/animals/{id}")
async def animal(id):
    return sql(f"SELECT * FROM animals WHERE id = '{id}'")