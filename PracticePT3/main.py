from fastapi import FastAPI, HTTPException, Request
from fastapi.responses import JSONResponse

app = FastAPI()

class UserNotFoundError(Exception):
    def __init__(self, name):
        self.name = name

@app.exception_handler(UserNotFoundError)
def errorHandler(request:Request, exe:UserNotFoundError):
    return JSONResponse(
        status_code=404,
        content= {
                "status" : "Error",
                "message":f"User {exe.name} not Found"
            }
         )
         


@app.get("/users/{name}")
def get_user(name:str):
    if name != "muskan":
        raise UserNotFoundError(name)
    else:
        return {
            "id" : 1,
            "name" : name
        }    