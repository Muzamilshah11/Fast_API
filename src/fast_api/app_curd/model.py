from sqlalchemy import Column, Integer, String
from .database import Base

class Employee(Base):
    __tablename__ = "employee_data"

    emp_id = Column(Integer, primary_key=True, index=True)
    emp_name = Column(String, index=True)
    emp_phone = Column(String)
    emp_address = Column(String)
    emp_salary = Column(Integer)

class Course(Base):
    __tablename__ = "courses"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String)