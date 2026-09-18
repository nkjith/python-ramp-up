"""
In Python, unpacking lets you assign or pass multiple values at once by expanding an iterable into individual items
"""

from pathlib import Path

HERE = Path(__file__).parent
csv_path = HERE / "resources" / "employees.csv"

a,b = 1,3
print(a,b)

# swap values
a, b = b, a
print(a,b)

# Starred targets

first, *middle, last = [1,2,3,4,5]
print(middle)

*x, y = 9,8,7,6,5

print(x)

# The variable with * is always a list even if its empty
a, *b = [1]
print(b) # --- []


"""
*args and **kwargs — unpacking in function calls
"""

## COLLECTING in functions

def total(*numbers):
    return sum(numbers)

print(total(1,2,3,4)) # numbers becomes (1, 2, 3, 4) — a tuple, automatically

## SPREADING at call site

climate = {"state": "Kerala", "temperature": 34}

def display_climate(state, temperature):
    print(state, temperature)

# ** on a dict at the call site unpacks it into key value pairs matching the argument names.
display_climate(**climate)


## Applying to employees.csv

def read_employees():
    with open(csv_path) as file:
        next(file)
        for row in file:
            name, city, department, salary = row.strip().split(",")
            yield name, city, department, int(salary) 


for name,city,department,salary in read_employees() :
    print(f"{name} works in {department} based in the city {city} for a salary of {salary}\n")

## Excercise => Write a function summarize(**kwargs) that accepts any number of named arguments and prints each one

def summarize(**kwargs):
    for key,value in kwargs.items():
        print(key, value)

summarize(name="ravi", role="engineer", years=11)

# data = ("ravi", "austin", "engineering", 95000, "senior") 
# Unpack this into name, salary, and a catch-all for everything in between — in one line, using *


data = ("ravi", "austin", "engineering", 95000, "senior") 
name, *_, salary, _ = data
print(name, salary)


