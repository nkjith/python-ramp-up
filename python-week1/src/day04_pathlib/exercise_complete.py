import csv
import json
from pathlib import Path

from pydantic import BaseModel, ConfigDict, Field, ValidationError

HERE = Path(__file__).parent
csv_path = HERE / "resources" / "employees_broken.csv"
output = csv_path.parent.parent / "output"

class Employee(BaseModel):
    model_config = ConfigDict(extra="forbid")
    name: str = Field(min_length = 1)
    city: str = Field(min_length = 1)
    department: str = Field(min_length = 1)
    salary: int = Field(gt=0)

def parse_row(line: int, record: dict) -> Employee | dict:
    try:
     return Employee.model_validate(record)
    except ValidationError as err:
        return( {
            "line": line,
            "record": record, 
            "error": [f"loc: {e['loc']} message: {e['msg']}" for e in err.errors()]
        } )


def read_employees(path : Path) -> tuple[list[Employee], list[dict]] :
    valid : list[Employee] = []
    errors : list[dict] = []

    with open(path, newline="") as file: # csv can have a single record with newline if its inside double quotes, we need this to take it as one record.
        reader = csv.DictReader(file, restkey="_extra") # rest key extra is needed to get the right error in validation if there is an extra column
        for line, record in enumerate(reader,start=2):
            value = parse_row(line, record)
            if (isinstance(value, Employee)):
                valid.append(value)
            else:
                errors.append(value)
    return valid, errors

def write_output(employees: list[Employee], errors: list[dict], out_dir: Path) -> None:
    out_dir.mkdir(exist_ok=True)
    json_path = out_dir / "employees.json"
    error_path = out_dir / "errors.json"
    employee_data = [employee.model_dump() for employee in employees]
    
    json_path.write_text(json.dumps(employee_data, indent=2))
    error_path.write_text(json.dumps(errors, indent=2))

def main() -> None:
    employees, errors = read_employees(csv_path)
    write_output(employees, errors, out_dir=output)

if __name__ == "__main__":
    main()

