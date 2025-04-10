# from typing import Union # When we use Mean's can assign the data type more then one at a time 
from fastapi import FastAPI
from enum import Enum
from pydantic import BaseModel

class Schema1(BaseModel): 
    id: int
    name: str
    roll_no: int


class AdvanceQuery(str, Enum): # Enum is like a list
    name1 = "name1"
    name2 = "name2"
    name3 = "name3" 

app = FastAPI() # Instance of FastAPI - like a Rebot

@app.get("/hello") # When someone visits the homepage, called Decorator in FastAPI
def read_root(): # Your robot’s reply.
    return {"message" : "Hello to fast-api.. testing mode"}

# @app.get("/items/{item_id}") # called Decorator in FastAPI
# async def path_fucn(item_id):
#     var_name = {"Path_Variable": item_id}
#     return var_name


# Query Parameter 1st Basic example
@app.get("/query") 
def query_Basic(name:str, roll_no: int): # Union[int,float, None] = None = None Means roll_no is optional. When we use Union that's me two are more then one type of data in one variable
    q_var = {"name": name, "roll no": roll_no} 
    return q_var

# Query Parameter Advance example
@app.get("/items/{model_name}")
async def query_Advance(model_name: AdvanceQuery):
    if model_name.value == "name1":
        return {"model_name": model_name, "message":"Calling model name 1"}
    if model_name.value == "name2":
        return {"model_name": model_name, "message":"Calling model name 2"}

    return {"model_name": model_name , "message":"without condition model name 3"}



# Request Body

@app.post("/schema1")
async def pydantic_fucn(data: Schema1):
    return f"This is your input Schema:-- {data}"


