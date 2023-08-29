from sqlalchemy.orm import Session
from models import Todo
from datetime import datetime

def add_todo(title:str, db:Session):
    current_time_stamp = datetime.now()
    convert_to_stamp = int(round(current_time_stamp.timestamp()))
    new_todo = Todo(
        title = title,
        created = convert_to_stamp,
        deadline = convert_to_stamp + 10800

    )
    db.add(new_todo)
    db.commit()
    db.refresh(new_todo)
    return new_todo

def update_todo(todo_id:int, db:Session):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    todo.complete = not todo.complete
    db.commit()

def delete_todo(todo_id:int, db:Session):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    db.delete(todo)
    db.commit()