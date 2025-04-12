# FastAPI and SQL (Relational) Databases
# Key Points
# No Forced Choice:
# FastAPI does not require you to use a SQL (relational) database. You have full freedom to choose whichever database (SQL or NoSQL) and ORM library fits your project needs.

# Using SQLModel:
# SQLModel is one option designed to work perfectly with FastAPI. It’s built on top of two popular libraries:

# SQLAlchemy: A powerful toolkit and Object Relational Mapper (ORM) for SQL databases.

# Pydantic: A library used in FastAPI for data validation using Python type annotations.

# SQLModel combines the best of both, letting you define Python classes that model your database tables while also performing automatic data validation and documentation.

# Supported Databases:
# Because SQLModel is built on top of SQLAlchemy, it supports every SQL database that SQLAlchemy does. This means you can easily work with:

# PostgreSQL

# MySQL

# SQLite

# Oracle

# Microsoft SQL Server

# …and any other database supported by SQLAlchemy.

# Other Options:
# You are free to use any other ORM (or even non-ORM libraries) depending on your requirements:

# For SQL Databases: Libraries like Django ORM, Peewee, or even raw SQL with libraries like aiomysql.

# For NoSQL Databases: Libraries such as Motor for MongoDB or others for Cassandra, Redis, etc.

# Practical Overview
# Flexibility with FastAPI:
# FastAPI is designed to work well regardless of the database choice. This means that your API endpoints and business logic are decoupled from the persistence layer. You can start with SQLModel if you're comfortable with a relational model, and later switch to another ORM or a NoSQL solution if your project needs change.

# Unified Data Models with SQLModel:
# SQLModel lets you define your data structures in one place. This definition serves two purposes:

# Database Model: It works as your SQL table schema.

# Data Validation: It validates the data input and output of your API endpoints automatically, thanks to Pydantic.

# This dual role keeps your code DRY (Don’t Repeat Yourself) and integrates seamlessly into FastAPI’s design pattern.

# Benefits of Using SQLModel:

# Simplicity: Define a single model and use it for both database interactions and API validation.

# Consistency: Ensures that the data flowing into your API matches the expectations of your database schema.

# Integration: Works naturally with FastAPI’s dependency injection system and auto-generated API docs.

# Expert-Level Perspective:
# With decades of professional experience, you can appreciate the design philosophy behind SQLModel and FastAPI – they help reduce boilerplate code and make your applications both easy to understand and maintain. This allows you to focus on solving business problems rather than wrestling with data conversion or validation issues.

# Code above omitted 👆
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

sqlite_file_name = "database.db"
sqlite_url = f"sqlite:///{My_First_DAtabase.db}"
connect_args = {"check_same_thread": False}
engine = create_engine(sqlite_url, connect_args=connect_args)

# Code below omitted 👇