from fast_api import FastAPI
from fastapi import Form

app = FastAPI()

@app.post("/login")
async def form_login(username: str = Form(...), password: str = Form(...)):
    return {"username": username, "Password": password}