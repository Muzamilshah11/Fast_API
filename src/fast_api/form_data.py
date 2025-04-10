from fastapi import FastAPI
from fastapi import Form

app = FastAPI()
# like Home page of a website
@app.get("/home")
async def home():
    return {"Hello": "World"}
@app.post("/login")
async def form_login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "Password": password}