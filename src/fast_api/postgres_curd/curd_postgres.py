from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

app = FastAPI()

# Define the Books schema using Pydantic
class Books(BaseModel):
    title: str       
    name: str        
    description: str 

# Database connection details
db_name = "fastapitest"
db_user = "postgres"
db_password = "1234"  # Replace with your actual password or use environment variable
db_host = "localhost"
db_port = "5432"

# Establish the database connection
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create the table when the application starts


# Create a new book entry and add it to the database
@app.post("/book")
def create_book(book: Books):
    try:
        with conn.cursor() as cursor:
            insert_query = "INSERT INTO book (title, name, description) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (book.title, book.name, book.description))
            conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return book

# Retrieve a book entry by its title
@app.get("/book/{title}")
def get_book(title: str):
    try:
        with conn.cursor() as cursor:
            select_query = "SELECT * FROM book WHERE title = %s"
            cursor.execute(select_query, (title,))
            book = cursor.fetchone()
            if book is None:
                raise HTTPException(status_code=404, detail="Book not found")
            return {"title": book[0], "name": book[1], "description": book[2]}
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# Update an existing book entry by its title
@app.put("/book/{title}")
def update_book(title: str, book: Books):
    try:
        with conn.cursor() as cursor:
            update_query = "UPDATE book SET name = %s, description = %s WHERE title = %s"
            cursor.execute(update_query, (book.name, book.description, title))
            conn.commit()
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return book

# Delete a book entry by its title
@app.delete("/book/{title}")    
def delete_book(title: str):
        try:
            with conn.cursor() as cursor:
                delete_query = "DELETE FROM book WHERE title = %s"
                cursor.execute(delete_query, (title,))
                conn.commit()
        except Exception as e:
            print(f"Database error: {e}")
            raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
        return {"message": "Book deleted successfully"}
                    
