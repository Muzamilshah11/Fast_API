from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import psycopg2

# Create a FastAPI app (like a toy shop where we manage our books)
app = FastAPI()

# Define what a book looks like (like a form for book details)
class NoteBook(BaseModel):
    title: str       # The book's title (e.g., "Harry Potter")
    name: str        # The author's name (e.g., "J.K. Rowling")
    description: str # A short description (e.g., "A magical adventure")

# Database connection details (like the address of our toy box)
db_name = "fastapitest"
db_user = "postgres"
db_password = "1234"  # Replace with your actual password
db_host = "localhost"
db_port = "5432"

# Connect to the database (open the toy box)
conn = psycopg2.connect(
    dbname=db_name,
    user=db_user,
    password=db_password,
    host=db_host,
    port=db_port
)

# Create the notebook table when the app starts (like setting up a new drawer for books) @app.on_event("startup")
def create_table():
    try:
        with conn.cursor() as cursor:
            cursor.execute("""
                CREATE TABLE IF NOT EXISTS notebook (
                    title TEXT,
                    name TEXT,
                    description TEXT
                )
            """)
            conn.commit()
    except Exception as e:
        print(f"Error creating table: {e}")

# Add a new book to the database (put a new notebook in the drawer)
@app.post("/notebook")
def create_book(nbook: NoteBook):
    try:
        with conn.cursor() as cursor:
            insert_query = "INSERT INTO notebook (title, name, description) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (nbook.title, nbook.name, nbook.description))
            conn.commit()  # Save the new book
    except Exception as e:
        print(f"Database error: {e}")
        raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
    return nbook

# # Find a book by its title (look for a book in the drawer)
# @app.get("/notebook/{title}")
# def get_book(title: str):
#     try:
#         with conn.cursor() as cursor:
#             select_query = "SELECT * FROM notebook WHERE title = %s"
#             cursor.execute(select_query, (title,))
#             nbook = cursor.fetchone()
#             if nbook is None:
#                 raise HTTPException(status_code=404, detail="NOte Book not found")
#             return {"title": nbook[0], "name": nbook[1], "description": nbook[2]}
#     except Exception as e:
#         print(f"Database error: {e}")
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")

# # Update a book's details by its title (change a book's info in the drawer)
# @app.put("/notebook/{title}")
# def update_book(title: str, nbook: NoteBook):
#     try:
#         with conn.cursor() as cursor:
#             update_query = "UPDATE notebook SET name = %s, description = %s WHERE title = %s"
#             cursor.execute(update_query, (nbook.name, nbook.description, title))
#             conn.commit()  # Save the changes
#     except Exception as e:
#         print(f"Database error: {e}")
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
#     return nbook

# # Delete a book by its title (remove a book from the drawer)
# @app.delete("/notebook/{title}")
# def delete_book(title: str):
#     try:
#         with conn.cursor() as cursor:
#             delete_query = "DELETE FROM notebook WHERE title = %s"
#             cursor.execute(delete_query, (title,))
#             conn.commit()  # Save the changes
#     except Exception as e:
#         print(f"Database error: {e}")
#         raise HTTPException(status_code=500, detail=f"Database error: {str(e)}")
#     return {"message": "NoteBook deleted successfully"}