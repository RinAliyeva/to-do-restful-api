from fastapi import FastAPI
from app.database import Base, engine
from app.api import users, tasks

Base.metadata.create_all(bind=engine)

app = FastAPI()

app.include_router(users.router, prefix="/api")
app.include_router(tasks.router, prefix="/api")

@app.get("/")
def read_root():
    return {"message": "Welcome to the ToDo API"}