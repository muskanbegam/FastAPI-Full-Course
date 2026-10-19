from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "assalmuwalikum"}

@app.get("/about")
def about():        
    return {"page": "about"}

@app.post("/create")
def create(name: str):
    return {"received": name}   

@app.get("/users/{user_id}")
def get_user(user_id: int):
    return {"user_id": user_id}
