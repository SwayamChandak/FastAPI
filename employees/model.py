from sqlalchemy import Column, String, Integer
from db import Base


class Employee(Base):
    __tablename__='employee'

    id=Column(Integer, primary_key=True, autoincrement=True, index=True)
    name=Column(String)
    email = Column(String(255), unique=True, nullable=False)
    dept=Column(String(255), nullable=False)