# Define an Employee dataclass and rewrite read_employees to yield instances instead of tuples: python

from collections.abc import Iterator
from dataclasses import dataclass
from pathlib import Path

HERE = Path(__file__).parent
csv_path = HERE / "resources" / "employees.csv"

@dataclass
class Employee:
    name: str
    city: str
    dept: str
    salary: int

def read_employees(path: Path) -> Iterator[Employee]:
    with open(path) as file:
        next(file)
        for row in file:
            name, city, dept, salary = row.strip().split(",")
            yield Employee(name, city, dept, int(salary))

emp1 = read_employees(csv_path)
print(next(emp1))

