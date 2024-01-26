#To define the model of the employee table
from pydantic import BaseModel, Field, constr
from typing import Optional
from datetime import date
from enum import Enum

#To create enumeration for department
class Department(str, Enum):
    admin = "admin"
    engineering = "engineering"
    management = "management"
    sales = "sales"
    qc = "qc"

#Model of the employee table
class Employee(BaseModel):
    fullName: str
    dateOfBirth: date
    dateJoined: date
    dateLeft: Optional[date]
    nric: str = Field(..., min_length=12, max_length=12, pattern='^[0-9]+$')
    department: Department
    salary: float
    remark: str