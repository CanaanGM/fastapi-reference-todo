
from fastapi import APIRouter, Depends, HTTPException
from ..models import models
from ..Data.database import engine, get_db
from .auth import *
from sqlalchemy.orm import Session


todo_router = APIRouter()


@todo_router.post("/todo")
async def create_todo(todo: models.TodoDto,user: dict=Depends(get_current_user), db: Session = Depends(get_db)):
    """auto mapper is a life saver!"""
    if user is None:
        raise HTTPException(404, "Nope")
    todo_model = models.Todo()
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo_model.complete
    if todo_model.complete: 
        todo_model.date_completed = datetime.utcnow()
        
    elif not todo_model.complete:
        todo_model.date_completed = None
    todo_model.owner_id = user.get("id")
    try:
        db.add(todo_model)
        db.commit()
        return {"status":201, "success":todo_model.id}
    except Exception as ex:
        return {"status":"Failure"}


@todo_router.get("/todo")
async def read_todos(user: dict=Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(404, "Nope")
    return db.query(models.Todo).filter(models.Todo.owner_id == user.get("id")).all()


@todo_router.get("/todo/user")
async def read_todos_by_user( user: dict=Depends(get_current_user) ,db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(404, "Nope")
    return db.query(models.Todo).filter(models.Todo.owner_id == user.get("id")).all()

@todo_router.get("/todo/{id}")
async def read_todo(id:int, user:dict = Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(404, "Nope")
    
    todo = db.query(models.Todo).filter(models.Todo.id == id).filter(models.Todo.owner_id == user.get("id")).first()

    if todo is not None:
        return  todo
    else:
         raise HTTPException(status_code=404, detail="Todo doesn't exist")

@todo_router.put("/{id}")
async def update_todo(id : int, todo: models.TodoDto, user: dict=Depends(get_current_user), db: Session = Depends(get_db)):
    if user is None:
        raise HTTPException(404, "Nope")
    todo_model = db.query(models.Todo).filter(models.Todo.id == id).filter(models.Todo.owner_id == user.get("id")).first()
    if todo_model is None:
        raise HTTPException(404, detail="Not Found")
    
    todo_model.title = todo.title
    todo_model.description = todo.description
    todo_model.priority = todo.priority
    todo_model.complete = todo_model.complete
    if todo_model.complete: 
        todo_model.date_completed = datetime.utcnow()
    elif not todo_model.complete:
        todo_model.date_completed = None

    try:
        db.add(todo_model)
        db.commit()
        return {"status":201, "success":todo_model.id}
    except Exception as ex:
        return {"status":"Failure"}


@todo_router.delete("/todo/{id}")
async def delete_todo(id:int,user: dict=Depends(get_current_user),  db: Session = Depends(get_db)):
    todo = db.query(models.Todo).filter(models.Todo.id == id).first()

    if todo is None:
         raise HTTPException(status_code=404, detail="Todo doesn't exist")
   
    try:
        db.query(models.Todo).filter(models.Todo.id == todo.id).filter(models.Todo.owner_id == user.get("id")).delete()
        db.commit()
        return {"Success":"todo died !"}
    except:
        raise HTTPException(status_code=500, detail="an error has Occu'd")   
