"""
One of the primary ways of defining schema in Pydantic is via models. 
Models are simply classes which inherit from BaseModel and define fields as annotated attributes.

We use the term “validation” to refer to the process of instantiating a model (or other type)
that adheres to specified types and constraints. 
This task, which Pydantic is well known for, is most widely recognized as “validation”.
"""

from pydantic import BaseModel, ConfigDict, field_validator


class Employee(BaseModel):
    model_config = ConfigDict(strict=True, str_strip_whitespace=True) # class attribute where you put model-level settings. It configures the whole model, not individual fields.
    salary : int
    name: str

# model_validate -- validate a dict against our model schema

data = {"name": "Ravi", "salary": 950000}

Employee.model_validate(data)

data = {"name": "Ravi"}

# Employee.model_validate(data) # Field required [type=missing, input_value={'name': 'Ravi'}, input_type=dict]

# model_validate_json — validate a JSON string

json_str = '{"name": "Ravi", "salary": 95000}'

emp = Employee.model_validate_json(json_str)

## model_dump -- to output

print(emp.model_dump()) # -- {'salary': 95000, 'name': 'Ravi'}

print(emp.model_dump_json()) # -- {"salary":95000,"name":"Ravi"}

### Nested models

class Address(BaseModel):
    city: str
    country: str

class Employee(BaseModel):
    name: str
    address: Address
    skills: list[str]

emp = Employee.model_validate({
    "name": "Ravi",
    "address": {"city": "Austin", "country": "US"},
    "skills": ["python", "sql"],
})
print(emp.address.city)     # Austin

# The nested dict becomes an Address object automatically, validated. 
# This is where pydantic starts doing real work — validating arbitrarily deep structures in one call.

### Field Validators

"""
Because @field_validator is designed to register the function as a class-level validator. Pydantic calls it in the context of the Employee model class.
"""

class NewEmployee(BaseModel):
    name: str
    salary: int

    @field_validator("name")
    @classmethod
    def name_must_be_titleCase(cls, v: str) -> str : 
        # @field_validator("name") tells Pydantic : Before accepting the name field,
        #  run this function to validate/transform its value
        # it can validate and transform the value
        return v.title()

emp_n = NewEmployee(name="john doe", salary=98000)
print(emp_n.name) # will print John Doe
