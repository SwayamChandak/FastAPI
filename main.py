from fastapi import FastAPI, Depends
from db import init_db
from employees.emps import emp_router as router

init_db()
app=FastAPI()

app.include_router(router)