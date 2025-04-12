from sqlalchemy.orm import Session
from . import models, schema

# Create an employee
def create_employee(db: Session, employee: schema.EmployeeCreate):
    db_employee = models.Employee(**employee.dict())
    db.add(db_employee)
    db.commit()
    db.refresh(db_employee)
    return db_employee

# Read all employees
def get_all_employees(db: Session):
    return db.query(models.Employee).all()

# Read an employee by ID
def get_employee_by_id(db: Session, emp_id: int):
    return db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()

# Update an employee
def update_employee(db: Session, emp_id: int, employee: schema.EmployeeCreate):
    db_employee = db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()
    if db_employee:
        for key, value in employee.dict().items():
            setattr(db_employee, key, value)
        db.commit()
        db.refresh(db_employee)
    return db_employee

# Delete an employee
def delete_employee(db: Session, emp_id: int):
    db_employee = db.query(models.Employee).filter(models.Employee.emp_id == emp_id).first()
    if db_employee:
        db.delete(db_employee)
        db.commit()
    return db_employee