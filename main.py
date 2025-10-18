from fastapi import FastAPI

api = FastAPI()

todo_list = [
    {"id": 1, "task": "Buy groceries", "completed": False},
    {"id": 2, "task": "Read a book", "completed": True},
    {"id": 3, "task": "Go for a walk", "completed": False},
    {"id": 4, "task": "Write code", "completed": True},
    {"id": 5, "task": "Clean the house", "completed": False}
]

@api.get("/")
def index():
    return {"message": "Hello, World!"}

@api.get("/todos")
def get_todos(first_n:int = None):
    if first_n is not None:
        return todo_list[:first_n]
    return todo_list   

@api.get("/todos/{todo_id}")
def get_todo_by_id(todo_id: int):
    for todo in todo_list:
        if todo["id"] == todo_id:
            return todo
    return {"error": "Todo not found"}   