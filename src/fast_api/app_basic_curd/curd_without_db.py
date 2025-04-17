from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()  # Create an instance of FastAPI

data: list = []  # This list simulates our "Database"

# Define the Books schema using Pydantic
class Books(BaseModel):
    title: str       # The title of the book
    name: str        # The name identifier for the book
    description: str # A brief description of the book

# Create a new book entry and add it to the "database"
@app.post("/book")
def create_book(book: Books):
    data.append(book.dict())  # Convert the Pydantic model to a dict and append it
    return data

# Retrieve a book entry by its index (id)
@app.get("/{id}")
def get_book(id: int):
    return data[id]  # Return the book entry at the provided index

# Update an existing book entry by its index (id)
@app.put("/book/{id}")
def update_book(id: int, book: Books):
    data[id] = book.dict()  # Replace the existing entry with the new data
    return data

# Delete a book entry by its index (id)
@app.delete("/book/{id}")
def delete_book(id: int):
    data.pop(id)  # Remove the entry at the given index
    return data # retun data
    


# Run the app when executing this file directly
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)

# How to run:
# 1. With the main function: Run "python <filename>.py" (e.g., python curd.py)
# 2. Without using the main: Run "uvicorn curd:app --reload" in your terminal 