from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI() # instance

data = []

class Books(BaseModel): # schema
    id: int
    name: str
    description: str

@app.get("/") # decorator
def read_root():
    return {"message": "Hello, the Book Hub!"}

@app.post("/books") # endpoint or Route
def create_book(book: Books):
    data.append(book.dict())
    return books 