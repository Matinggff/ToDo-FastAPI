from fastapi import FastAPI,Request ,Depends, status, Form
from fastapi.templating import Jinja2Templates
from database import engine, get_db
import models
from starlette. responses import RedirectResponse
from sqlalchemy.orm import Session
from models import Todo
import orm
from datetime import datetime

app = FastAPI()

models.Base.metadata.create_all(bind=engine)

templates = Jinja2Templates("templates")

@app.get("/")
def home(request: Request, db: Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return templates.TemplateResponse("index.html", {"request": request, "todo_list": todos})

@app.post("/add")
def add(request: Request, title:str = Form(...), db: Session = Depends(get_db)):
    orm.add_todo(title, db)
    
    url = app.url_path_for("home") #def name
    return  RedirectResponse(url, status_code=status.HTTP_303_SEE_OTHER)

@app.get("/update/{todo_id}")
def update(request: Request, todo_id: int, db: Session = Depends(get_db)):
    orm.update_todo(todo_id, db)
    url = app.url_path_for("home")
    return RedirectResponse(url, status_code=status.HTTP_302_FOUND)

@app.get("/delete/{todo_id}")
def delete(request: Request, todo_id: int, db: Session = Depends(get_db)):
    orm.delete_todo(todo_id, db)
    url = app.url_path_for("home")
    return RedirectResponse(url, status_code=status.HTTP_302_FOUND)

@app.get("/time/{todo_id}")
def time_left(request: Request, todo_id: int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    current_time = datetime.now()
    convert_to_stamp = int(round(current_time.timestamp()))
    todo_left = todo.deadline - convert_to_stamp
    todo.left_time = todo_left
    db.commit()
    url = app.url_path_for("home")
    return RedirectResponse(url, status_code=status.HTTP_302_FOUND)




    