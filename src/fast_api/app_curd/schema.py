from pydantic import BaseModel, Field, constr

# Employee Schemas
class EmployeeCreate(BaseModel):
    emp_name: str = Field(..., min_length=2, max_length=100)
    emp_phone: constr(regex=r'^\d{10}$')
    emp_address: str = Field(..., min_length=5, max_length=255)
    emp_salary: int = Field(..., gt=0)

class Employee(BaseModel):
    emp_id: int
    emp_name: str
    emp_phone: str
    emp_address: str
    emp_salary: int

    class Config:
        orm_mode = True

# Course Schemas
class CourseCreate(BaseModel):
    title: str
    description: str

class Course(BaseModel):
    id: int
    title: str
    description: str

    class Config:
        orm_mode = True