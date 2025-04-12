# from sqlalchemy import create_engine
# from sqlalchemy.orm import declarative_base, sessionmaker
# from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# from sqlalchemy.orm import relationship

# SQLALCHEMY_DATABASE_URL = "sqlite:///./my_first_database.db"

# engine = create_engine(SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False})

# SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base = declarative_base()

# class User(Base):
#     __tablename__ = "users"

#     id = Column(Integer, primary_key=True, index=True)
#     email = Column(String, unique=True, index=True)
#     hashed_password = Column(String)
#     is_active = Column(Boolean, default=True)

#     items = relationship("Item", back_populates="owner")

# class Item(Base):
#     __tablename__ = "items"

#     id = Column(Integer, primary_key=True, index=True)
#     title = Column(String, index=True)
#     description = Column(String, index=True)
#     owner_id = Column(Integer, ForeignKey("users.id"))

#     owner = relationship("User", back_populates="items")

    
# # Explanation of database.py:
# # •
# # It imports necessary modules from SQLAlchemy.
# # •
# # SQLALCHEMY_DATABASE_URL defines the connection string for the database. Here, it's set up to use a SQLite database file named my_first_database.db located in the current directory.
# # •
# # create_engine creates the SQLAlchemy engine, which is responsible for connecting to the database. The connect_args parameter is specific to SQLite and prevents issues with threading [This information is not directly in the sources but is common practice with SQLite and FastAPI].
# # •
# # SessionLocal creates a factory for database sessions. Each request to your FastAPI application will typically use its own database session [This information is not directly in the sources but is a standard pattern in FastAPI].
# # •
# # Base = declarative_base() creates a base class for your SQLAlchemy models.
# # •
# # The User class defines the users table with columns for id, email, hashed_password, and is_active. It also establishes a relationship with the Item model through the items attribute.
# # •
# # The Item class defines the items table with columns for id, title, description, and owner_id. owner_id is a foreign key that references the id column of the users table. The owner attribute establishes the reverse relationship with the User model.


# python "src\fast_api\app_db\generate_employee_data.py" add teminal then run
import psycopg2
import csv

# Database connection parameters (update these with your actual values)
db_params = {
    "database": "tutorials",
    "user": "postgres",
    "password": "test123",
    "host": "localhost",
    "port": "5432",
}

# Path to the CSV file
csv_file_path = "employee_data.csv"

try:
    # Connect to the PostgreSQL database
    conn = psycopg2.connect(**db_params)
    cursor = conn.cursor()

    # Ensure the Employee_Data table exists (optional, if not already created)
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS Employee_Data (
            emp_id INTEGER PRIMARY KEY,
            emp_name VARCHAR(100),
            emp_phone VARCHAR(15),
            emp_address VARCHAR(255),
            emp_salary INTEGER
        );
    """)

    # Use COPY to import the CSV file
    with open(csv_file_path, "r") as f:
        cursor.copy_expert(
            sql="COPY Employee_Data (emp_id, emp_name, emp_phone, emp_address, emp_salary) FROM STDIN WITH CSV HEADER DELIMITER ','",
            file=f
        )

    # Commit the transaction
    conn.commit()
    print("CSV data imported successfully into Employee_Data table!")

    # Verify the data
    cursor.execute("SELECT * FROM Employee_Data;")
    rows = cursor.fetchall()
    for row in rows:
        print(row)

except Exception as e:
    print(f"An error occurred: {e}")
    conn.rollback()

finally:
    # Close the database connection
    cursor.close()
    conn.close()