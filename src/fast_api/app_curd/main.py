# from fastapi import FastAPI, HTTPException, Depends
# from typing import List
# from sqlalchemy.orm import Session
# from .database import Base, engine, SessionLocal
# from . import models, schema, crud

# # Create the FastAPI app
# app = FastAPI()

# # Create the database tables
# models.Base.metadata.create_all(bind=engine)


# # Dependency to get the database session
# def get_db():
#     db = SessionLocal()
#     try:
#         yield db
#     finally:
#         db.close()

# db_dependency = Depends(get_db)

# # Course Endpoints (unchanged)
# @app.get("/courses/", response_model=List[schema.Course])
# async def get_all_courses(db: Session = db_dependency):
#     courses = db.query(models.Course).all()
#     return courses

# @app.post("/courses/", response_model=schema.Course)
# async def create_course(course: schema.CourseCreate, db: Session = db_dependency):
#     db_course = models.Course(**course.dict())
#     db.add(db_course)
#     db.commit()
#     db.refresh(db_course)
#     return db_course

# @app.get("/courses/{course_id}", response_model=schema.Course)
# async def get_course_by_id(course_id: int, db: Session = db_dependency):
#     course = db.query(models.Course).filter(models.Course.id == course_id).first()
#     if course is None:
#         raise HTTPException(status_code=404, detail="No course found")
#     return course

# # Employee Endpoints (using CRUD functions)
# @app.get("/employees/", response_model=List[schema.Employee])
# async def get_all_employees(db: Session = db_dependency):
#     return crud.get_all_employees(db)

# @app.post("/employees/", response_model=schema.Employee)
# async def create_employee(employee: schema.EmployeeCreate, db: Session = db_dependency):
#     return crud.create_employee(db, employee)

# @app.get("/employees/{emp_id}", response_model=schema.Employee)
# async def get_employee_by_id(emp_id: int, db: Session = db_dependency):
#     employee = crud.get_employee_by_id(db, emp_id)
#     if employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return employee

# @app.put("/employees/{emp_id}", response_model=schema.Employee)
# async def update_employee(emp_id: int, employee: schema.EmployeeCreate, db: Session = db_dependency):
#     updated_employee = crud.update_employee(db, emp_id, employee)
#     if updated_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return updated_employee

# @app.delete("/employees/{emp_id}")
# async def delete_employee(emp_id: int, db: Session = db_dependency):
#     deleted_employee = crud.delete_employee(db, emp_id)
#     if deleted_employee is None:
#         raise HTTPException(status_code=404, detail="Employee not found")
#     return {"message": "Employee deleted successfully"}

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def read_root():
    return {"message": "Hello, World"}