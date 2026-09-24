from pathlib import Path

HERE = Path(__file__).parent
csv_path = HERE / "resources" / "employees.csv"

"""
A1. Given nums = [4, 7, 2, 9, 1, 8], produce a list of the squares of only the odd numbers. One line.

A2. Given words = ["python", "go", "rust", "javascript"], produce a dict mapping each word to its length, but only for words with 4 or more characters. One line.

A3. Given data = (1, 2, 3, 4, 5, 6), unpack so that first = 1, last = 6, and middle holds everything else. One line.

A4. Given price = 1234.5678, print it as $1,234.57. One f-string.
"""

# A1
nums = [4, 7, 2, 9, 1, 8]

squares = [n*n for n in nums if n%2 != 0]

print(squares)

# A2
words = ["python", "go", "rust", "javascript"]

word_dict = {word: len(word) for word in words if len(word) >= 4}

print(word_dict)

# A3
data = (1, 2, 3, 4, 5, 6)

first, *middle, last = data

# A4
price = 1234.5678

print(f"${price:,.2f}")


"""
B1. Write a generator function read_employees(path) that yields a tuple of (name, city, dept, salary) for each employee, skipping the header, with salary as an int. Then use it to print a numbered list starting at 1, formatted like:

1. Ravi Kumar — Engineering — $95,000
"""

def read_employees(path):
    with open(path) as f:
        next(f)
        for row in f:
            name, city, dept, salary = row.strip().split(",")
            yield name, city, dept, int(salary)

employee = read_employees(csv_path)

for i, (name, _, dept, salary) in enumerate(employee, start=1):
    print(f"{i}. {name} - {dept} - ${salary:,}")

"""
B2. Using read_employees, build a dict of {name: salary} for Engineering employees only. One dict comprehension. (You should get 4 entries.)
"""

eng_employees = read_employees(csv_path)

emp_dict = {name:salary for name, _,dept, salary in eng_employees if dept=='Engineering'}

print(emp_dict)

"""
B3. Count how many employees earn more than 80,000 — without building a list. One line, using sum().
"""

num_employees = [sum([1 for _,_,_, salary in read_employees(csv_path) if salary>80000 ])]

print(num_employees)

"""
B4. Given these two lists:

python
cities = ["Austin", "Tacoma", "Topeka"]
temps = [95, 68, 82]

Print each as Austin: 95°F, numbered from 1. Use enumerate, zip, and an f-string in a single loop.
"""

cities = ["Austin", "Tacoma", "Topeka"]
temps = [95, 68, 82]

for i, (city, temp) in enumerate(zip(cities,temps), start=1):
    print(f"{i}. {city}: {temp}°F")
