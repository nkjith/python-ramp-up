import csv
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, ValidationError

HERE = Path(__file__).parent
BROKEN_CSV = HERE / "resources" / "employees_broken.csv"


class Employee(BaseModel):
    model_config = ConfigDict(extra="forbid")

    name: str = Field(min_length=1)
    city: str = Field(min_length=1)
    dept: str = Field(min_length=1, alias="department")
    salary: int = Field(gt=0)


def read_employees(path: Path) -> tuple[list[Employee], list[dict]]:
    valid: list[Employee] = []
    errors: list[dict] = []

    with open(path, newline="") as file:
        reader = csv.DictReader(file, restkey="_extra")

        for line_num, record in enumerate(reader, start=2):
            try:
                valid.append(Employee.model_validate(record))
            except ValidationError as e:
                errors.append({
                    "line": line_num,
                    "row": record,
                    "error": [f"{err['loc'][0]}: {err['msg']}" for err in e.errors()],
                })

    return valid, errors


def main() -> None:
    employees, errors = read_employees(BROKEN_CSV)

    print(f"{len(employees)} valid, {len(errors)} invalid\n")
    for emp in employees:
        print(f"  {emp.name:<20} {emp.dept:<15} ${emp.salary:,}")

    print("\nErrors:")
    for err in errors:
        print(f"  line {err['line']}: {err['error']}")
        print(f"    {err['row']}")


if __name__ == "__main__":
    main()