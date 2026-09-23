"""
Make a deliberately broken CSV (negative salary, empty name, salary as "abc", a missing column). 
Write a reader that collects valid employees and invalid rows separately:
"""

from pathlib import Path

from pydantic import BaseModel, Field, ValidationError

HERE = Path(__file__).parent
broken_csv_path = HERE / "resources" / "employees_broken.csv"


class Employee(BaseModel):
    name: str = Field(min_length=1)
    city: str = Field(min_length=1)
    dept: str = Field(min_length=1)
    salary: int = Field(gt=0)

def read_employees(path: Path) -> tuple[list[Employee], list[dict]]:

    valid_employees : list[Employee] = []
    errors: list[dict] = []
    with open(path) as file:
        next(file)
        for line_num, row in enumerate(file, start=2):
            row = row.strip()
            if not row:
                continue
            # first see if there are any columns missing
            try:
                name, city, dept, salary = row.split(",")
            except ValueError as e:
                errors.append({
                    "line": line_num,
                    "row": row,
                    "error": f"wrong number of columns {e}"
                })
                continue

            try:
                valid_employees.append(
                    Employee(name=name, city= city, dept=dept, salary=salary)
                )
            except ValidationError as e:
                errors.append({
                                    "line": line_num,
                                    "row": row,
                                    "error": [f"{err['loc']}: {err['msg']}" for err in e.errors()]
                                })
                continue

    return valid_employees, errors


employees, errors = read_employees(broken_csv_path)

print(f"{len(employees)} valid, {len(errors)} invalid\n")

for emp in employees:
    print(f"  {emp.name:<20} {emp.dept:<15} ${emp.salary:,}")

print("\nErrors:")
for err in errors:
    print(f"  line {err['line']}: {err['error']}")
    print(f"    {err['row']}")