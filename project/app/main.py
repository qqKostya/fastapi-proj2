from fastapi import Depends, FastAPI
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from .db import get_session, init_db
from .models import Employee, EmployeeCreate

app = FastAPI()


@app.get("/ping")
async def pong():
    return {"ping": "pong!"}


@app.get("/employee", response_model=list[Employee])
async def get_employee(session: AsyncSession = Depends(get_session)):
    result = await session.execute(select(Employee))
    employee = result.scalars().all()
    return [
        Employee(
            full_name=empl.full_name,
            job_title=empl.job_title,
            employment_date=empl.employment_date,
            salary=empl.salary,
            id_chief=empl.id_chief,
            id=empl.id,
        )
        for empl in employee
    ]


@app.post("/employee")
async def add_employee(
    empl: EmployeeCreate, session: AsyncSession = Depends(get_session)
):
    empl = Employee(
        full_name=empl.full_name,
        job_title=empl.job_title,
        employment_date=empl.employment_date,
        salary=empl.salary,
        id_chief=empl.id_chief,
    )
    session.add(empl)
    await session.commit()
    await session.refresh(empl)
    return empl
