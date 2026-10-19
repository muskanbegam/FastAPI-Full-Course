from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

todos = []

class Todo(BaseModel):
    id: int
    task: str
    completed: bool

@app.post("/todos")
def create_todo(todo:Todo):
    todos.append(todo)
    return {"message": "TODO added", 
            "data": todos}

@app.get("/todos")
def get_todos():
    return todos

@app.get("/todos/{todos_id}")
def get_todo_by_id(todos_id:int):
    for todo in todos:
        if todo.id == todos_id: 
            return todo
    return {"error":"Todo Not Found"}