from typing import Optional

from sqlmodel import SQLModel, Field


class EmployeeBase(SQLModel):
    full_name: str
    job_title: str
    employment_date: str
    salary: int
    id_chief: Optional[int] = None


class Employee(EmployeeBase, table=True):
    id: int = Field(default=None, primary_key=True)


class EmployeeCreate(EmployeeBase):
    pass
