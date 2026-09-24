"""
pydantic is a library that allows you to do data validation and serialization for data
work with data which is not well structured -- pydantic can help validate that early on.
Pydantic adds much more validations and serializations than data class. 
Fastest data validation library available
"""

from datetime import datetime
from enum import Enum

from pydantic import BaseModel, Field


class Department(Enum):
    ENGINEERING = "engineering"

class Employee(BaseModel):
    name:str
    city:str
    dept:str
    salary:int

# emp_1 = Employee('Nimisha','TVM','Engineering',95000) # ----> type error since pydantic needs explicit names parameters

emp_1 = Employee(name='Nimisha',city='TVM',dept=Department.ENGINEERING.value,salary=95000)

print(emp_1)

# Coercion - it makes conversion when its sensible

emp_2 = Employee(name='Nimisha',city='TVM',dept=Department.ENGINEERING.value,salary="95000")

print(type(emp_1.salary)) # <class 'int'>

# Defaults
class Employee(BaseModel):
    name: str
    salary: int = 50000
    tags: list[str] = []        # SAFE here — pydantic copies it per instance

# Note: unlike dataclasses, pydantic handles mutable defaults correctly. 
# You don't need default_factory for the common case. It exists for computed defaults:

class Document(BaseModel):
    created: datetime = Field(default_factory=datetime.now)



