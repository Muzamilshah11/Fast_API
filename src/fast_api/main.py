
from fastapi import FastAPI

app = FastAPI() # Instance of FastAPI - like a Rebot 

@app.get("/hello") # When someone visits the homepage, say hello. also PATH VARIABLE OR PARAMETER    
def read_root(): # Your robot’s reply.
    return {"message" : "Hello to fast-api.. testing mode"} 

# @app.get("/items/{item_id}")
# def read_item(item_id):
#     return {"item_id": item_id}

@app.get("/items/{item_id}")
async def path_para(item_id):
    var_name = {"Path Variable ":"item_id"}
    return var_name 