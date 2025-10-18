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

@api.post("/todos")
def add_todo(todo_data: dict):
    new_todo_id = max((t["id"] for t in todo_list), default=0) + 1
    new_todo = {
        "id": new_todo_id,
        "task": todo_data.get("task", ""),
        "completed": todo_data.get("completed", False)
    }
    todo_list.append(new_todo)
    return new_todo

@api.delete("/todos/{todo_id}")
def delete_todo(todo_id: int):
    for index, todo in enumerate(todo_list):
        if todo["id"] == todo_id:
            deleted_todo = todo_list.pop(index)
            return deleted_todo
    return {"error": "Todo not found"}

@api.put("/todos/{todo_id}")
def update_todo(todo_id:int, updated_todo:dict):
    for todo in todo_list:
        if todo['id'] == todo_id:
            todo.update(updated_todo)
            return todo
    return {"error": "Todo not found"} 