from typing import Union, Optional # When we use Mean's can assign the data type more then one at a time 
from fastapi import FastAPI, Query, Form, File, UploadFile
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


# Query Parameter 1st Basic example with Query validation too 
@app.get("/query")
def query_basic(
    name: Optional[str] = None,
    roll_no: Optional[str] = Query(default=None, min_length=2, max_length=5)): # min_length 12 limit 2, max 12345 just accecpt not more then 5 and not less then 2
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

#Form Data:-- Main d/f form data when we put data the in string form not query form

@app.post("/form/data")
async def form_data(username: str = Form(),    password: str = Form()):
    return {"username": username, "password": password}


# Form Data with pydantic validation
class FormSchema1(BaseModel): 
    id: int
    name: str
    roll_no: int
@app.post("/form/data/pydantic")
async def form_data_pydantic(data: FormSchema1 = Form()):
    return f"This is your input Schema:-- {data}" 


# File Upload through byte converter
@app.post("/file/upload")
async def file_upload_byte(file: bytes = File()): # UploadFile is a class in FastAPI then will get the file
    return {"file_size": len(file)}

@app.post("/upload/file")
async def upload_file(file: UploadFile): # UploadFile is a class in FastAPI then will get the file
    return {"filename": file} # show all the file details 
    # return {"filename": file.filename, "file_content_type": file.content_type}  # just show file name and content type   
 