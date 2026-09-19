"""
Type hints are annotations your editor and tools read to catch mistakes before you run anything.
More importantly for you: pydantic reads these annotations to know what to validate
"""

from typing import Any
from collections.abc import Iterator
from pathlib import Path

def print_names(first, last):
     print(f"{first.title()} {last.title()}")

print_names("nimisha","jith")

def get_full_name(first: str, last: str):
     print(f"{first.title()} {last.title()}") # --- will get suggestions here for methods

get_full_name("nimisha","jith")


def get_name_with_age(name: str, age: int):
    name_with_age = name + " is this old: " + str(age) 
    return name_with_age # -- convert age to str before concatenation


"""
typing module¶
For some additional use cases, you might need to import some things from the standard library typing module, 
for example when you want to declare that something has "any type", you can use Any from typing:

from typing import Any

"""

def testing(parameter1: Any):
     print("testing Any")


### Generic Types

"""
Some types can take "type parameters" in square brackets, to define their internal types,
for example a "list of strings" would be declared list[str].

list
tuple
set
dict
"""

def process_items(items: list[str]):
    for item in items:
        print(item)

# Union

"""
We can specify a variable can be one of multiple types
"""

def multiple(item : str | int):
     print(item)

# Classes as types

class Person:
    def __init__(self, name: str):
        self.name = name


def get_person_name(one_person: Person):
    return one_person.name


"""
Annotating generators

from collections.abc import Iterator
from pathlib import Path

def read_employees(path: Path) -> Iterator[tuple[str, str, str, int]]:
    ...

Iterator[...] is how you annotate a generator function.
"""



#TypeAlias — naming complex types

type Employee = tuple[str, str, str, int]
type SalaryReport = dict[str, list[tuple[str, int]]]

def read_employees(path: Path) -> Iterator[Employee]: ...
def salary_report(rows: Iterator[Employee]) -> SalaryReport: ...


# Literal — restrict to specific values

from typing import Literal

def set_mode(mode: Literal["read", "write", "append"]) -> None:
    ...

set_mode("delete")   # Pylance flags this