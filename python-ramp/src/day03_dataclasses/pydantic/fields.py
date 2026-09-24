"""
What Field() does

The annotation says what type a value is. Field() says what values of that type are acceptable.

Number constraints

Four of them, named after the comparison operators:

gt	greater than	> value
ge	greater than or equal	>= value
lt	less than	< value
le	less than or equal	<= value

"""

from pydantic import BaseModel, Field

salary: int                      # any integer — including -5000
salary: int = Field(gt=0)        # must be a positive integer

class Employee(BaseModel):
    salary: int = Field(gt=0, le=100000)

# String constraints

name:str = Field(min_length=1, max_length=10)

# description — not a constraint

dept: str = Field(description="Department name")

# Does nothing at runtime. It's metadata that shows up in the model's JSON Schema.
# Why it matters for you specifically: 
#   when you use a pydantic model to define structured output from an LLM, the schema — including these descriptions is what gets sent to the model.
#  The description is effectively part of your prompt

"""
Handling errors
"""
from pydantic import ValidationError

try:
    emp = Employee(name="", salary=-100)
except ValidationError as e:
    print(e.errors())
