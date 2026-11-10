from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker, Session
from fastapi import FastAPI, Depends, HTTPException

app = FastAPI()
DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL,
                       connect_args={"check_same_thread" : False})

sessionlocal = sessionmaker(bind = engine)

Base = declarative_base()

class Todo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index = True)
    todo = Column(String)   
    completed = Column(String)

Base.metadata.create_all(bind = engine)

def get_db():
    db = sessionlocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/")
def home(db:Session = Depends(get_db)):
    todos = db.query(Todo).all()
    return{
        "message":"db Connected",
        "total": len(todos),
        "data" : todos


    }
@app.post("/todos")
def create_db(todo:str,db:Session = Depends(get_db)):
    todo = Todo(todo = todo, completed = "False")
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return {
        "messgae":"Todo Created",
        "data": todo
    }

@app.get("/todos/{todo_id}")
def todo_id(todo_id:int, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail= "Todo not found")
    return todo

@app.put("/todos/{todo_id}")
def update_todo(todo_id:int, title: str, db: Session = Depends(get_db)):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if not todo:
        raise HTTPException(status_code=404, detail= "Todo not found")
    todo.todo = title
    db.commit()
    db.refresh(Todo)
    return{
        "message":"todo updated",
        "data updated":todo
    }
        


    








