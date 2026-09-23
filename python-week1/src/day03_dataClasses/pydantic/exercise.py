from collections.abc import Iterator
from pathlib import Path

from pydantic import BaseModel, Field

"""
4. Round-trip: build an Employee, model_dump_json() it, model_validate_json() it back, confirm equality.

5. Nested model — add an Address with city and country, restructure Employee to use it.

6. Define an Analysis model like the one above with a Literal sentiment field and a bounded confidence. Validate a hand-written JSON string against it, then break the JSON and watch the error.
"""

HERE = Path(__file__).parent
csv_path = HERE / "resources" / "employees.csv"

print(csv_path)


class Employee(BaseModel):
    name: str = Field(min_length=1)
    city: str
    dept: str
    salary: int = Field(gt=0)

def read_employee(path: Path) -> Iterator[Employee]:
    with open(path) as file:
        next(file)
        for row in file:
            name, city, dept, salary = row.strip().split(",")
            yield Employee(name=name, city=city, dept=dept, salary=salary)

emp_1 = read_employee(csv_path)

employee_1 = next(emp_1)

json_employee = Employee.model_dump_json(employee_1)

print(json_employee)