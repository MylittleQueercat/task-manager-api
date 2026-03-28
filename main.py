from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

tasks = []

class Task(BaseModel):
    title: str
    done: bool = False

@app.get("/")
def hello():
    return {"message": "Hello 42!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task

@app.delete("/tasks/{id}")
def delete_task(id: int):
    tasks.pop(id)
    return {"message": f"Task {id} deleted"}

@app.put("/tasks/{id}")
def update_task(id: int, updated_task: Task):
    tasks[id] = updated_task
    return updated_task