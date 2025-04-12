from typing import Annotated
from pydantic import BaseModel
from fastapi import FastAPI, Form

app = FastAPI() # Create Instance

@app.get("/home") 
def home():
    return {"message": "Hello EveryOne today topic is form data in FastAPI"} 

@app.post("/login/form")
# async def login(username: Annotated[str, Form()], password: Annotated[str, Form()]):
async def login(username:str = Form(), password:str = Form()):

    return {"username": username}


@app.post("/login/data")
async def form_login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "Password": password}


# Pydantic Validation with Form Data


class FormData(BaseModel):
    id:int
    f_name:str
    l_name:str
    contact_no: int
    address:str
    username: str
    password: str

@app.post("/pydantic/")
async def login(data: Annotated[FormData, Form()]):
    return data