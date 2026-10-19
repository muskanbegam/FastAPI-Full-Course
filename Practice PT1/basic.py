from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class User(BaseModel):
    name:str
    age:int

@app.get("/")
def home():
    return {"message":"Hello without vern"}

@app.get("/users")
def get_users(name:str = "No Name Provided"):
    return {"Name": name}

@app.post("/create-user")
def create_user(user:User):
    return{
        "message" : "User Created",
        "data": user
    }