from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).parent
csv_path = HERE / "resources" / "employees.csv"

"""
Part D — The real test

D1. Write a function salary_report(path) that returns a dict mapping each department to a list of (name, salary) tuples, sorted by salary descending within each department.

Expected shape:

python
{
    "Engineering": [("Vikram Singh", 112000), ("Suresh Reddy", 105000), ...],
    "Design": [...],
    ...
}

Then print it as:

Engineering
  Vikram Singh          $112,000
  Suresh Reddy          $105,000
  ...

You'll need: file reading, unpacking, a generator or comprehension, dict building, sorting with a key, and f-string formatting. Sorting isn't something we covered explicitly — look up sorted() with key= and reverse=. Figuring out an unfamiliar piece from docs is part of the exercise.
"""

def read_employees(path):
    with open(path) as f:
        next(f)
        for row in f:
            name, city, dept, salary = row.strip().split(",")
            yield name, city, dept, int(salary)



def salary_report(emp_reader):
    emp_dict = defaultdict(list)
    for name, _, dept, salary in emp_reader:
      emp_dict[dept].append((name, salary))

    for dept in emp_dict:
      emp_dict[dept].sort(key=lambda x:x[1], reverse=True)

    return emp_dict

final_report = salary_report(read_employees(csv_path))


print("\n\n******\n\n")

for dept, employees in final_report.items():
    print(dept)
    for name, salary in employees:
        print(f"  {name:<20} ${salary:,}")

