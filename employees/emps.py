from pydantic import BaseModel
from fastapi import APIRouter, Depends, HTTPException
from typing import Annotated, List
from sqlalchemy.orm import Session, joinedload
from init import get_db
from employees.model import Employee

db_dependecy=Annotated[Session, Depends(get_db)]
emp_router=APIRouter()

class EmpBase(BaseModel):
    name:str
    email:str
    dept:str

class EmpCreate(EmpBase):
    id:int
    

class EmpOut(EmpBase):
    pass

class EmpUpdate(EmpCreate):
    pass

@emp_router.get("/emp", response_model=List[EmpOut])
async def get_emp(db:db_dependecy):
    try:
        emps=db.query(Employee).all()
        print("All Employees found")
        if emps is not None:
            return emps
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    return []


@emp_router.get("/emp/{emp_id}", response_model=EmpOut)
async def get_single_emp(emp_id:int, db:db_dependecy):
    try:
        emp=db.query(Employee).filter(Employee.id==emp_id).first()
        if emp is not None:
            print(f"Found employee with employeeID {emp_id}")
            return emp
        else:
            raise HTTPException(status_code=404, detail="Can't find employee")
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    

@emp_router.post("/emp", response_model=EmpCreate)
async def add_emp(db: db_dependecy, new_emp:EmpBase):
    try:
        db_emp=Employee(name=new_emp.name, email=new_emp.email, dept=new_emp.dept)
        db.add(db_emp)
        db.commit()
        db.refresh(db_emp)
        print(f"Created and added new employee whose name is {new_emp.name}")
        return db_emp
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
    


@emp_router.delete("/emp/{emp_id}", response_model=EmpOut)
async def delete_emp(emp_id: int, db: db_dependecy):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    db.delete(emp)
    db.commit()
    return emp

@emp_router.put("/emp/{emp_id}", response_model=EmpOut)
async def update_emp(emp_id: int, emp_update: EmpUpdate, db: db_dependecy):
    emp = db.query(Employee).filter(Employee.id == emp_id).first()
    if emp is None:
        raise HTTPException(status_code=404, detail="Employee not found")
    emp.name = emp_update.name
    emp.email = emp_update.email
    emp.dept = emp_update.dept
    db.commit()
    db.refresh(emp)
    return emp