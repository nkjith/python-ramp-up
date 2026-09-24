import json
from datetime import datetime
from pathlib import Path

"""
4 functions - 

Read  - json.loads(s) --> s Vf=[] for string json.load(obj) str to dict --> to load from file
Write - json.dumps(s) --> s is for string json.dump(obj) dict to str --> to write to file
"""

data = {"name": "Ravi", "salary": 95000, "skills": ["python", "sql"]}

print(type(data))
text = json.dumps(data)
print(text) # -- type str

back = json.loads(text)
print(f"\nvalue - {back}, type - {type(back)}") # Python dicts print with ', JSON uses "

print(json.dumps(data, indent=2)) # readable

json.dumps(data, sort_keys=True)          # alphabetical keys — useful for diffs
json.dumps(data, ensure_ascii=False)      # keeps non-ASCII readable, e.g. "café" not "caf\u00e9"


print("\n\n New Exercise \n\n")

curr_directory = Path(__file__).parent
out_path = curr_directory / "output" / "test.json"
out_path.parent.mkdir(parents=True, exist_ok=True)
print(out_path)

with open(out_path,"w") as f:
    json.dump(data, f, indent=2)

with open(out_path,"r") as r:
    loaded = json.load(r)

print(loaded)

# For smaller files, skip open entirely

data["name"] = 'Nimisha'

out_path.write_text(json.dumps(data, indent=2))

text = out_path.read_text()
print(text)

dict_text = json.loads(out_path.read_text())
print(dict_text)

print("\n\nType Mapping\n\n")

python_obj = {
    "string": "text",
    "integer": 42,
    "float": 3.14,
    "boolean": True, # True becomes true
    "nothing": None, # becomes null
    "list": [1, 2, 3],
    "nested": {"a": 1},
    "tuple": (1,2,3,4) # becomes array and comes back as list
}

json_str = json.dumps(python_obj, indent=2)
print(json_str)

round_trip = json.loads(json_str)
print(round_trip) # {'string': 'text', 'integer': 42, 'float': 3.14, 'boolean': True, 'nothing': None, 'list': [1, 2, 3], 'nested': {'a': 1}, 'tuple': [1, 2, 3, 4]}


# by default json cannot handle set, path and date time objects in dump
#json.dumps({"when": datetime.now()})
# TypeError: Object of type datetime is not JSON serializable
# Fix - default is called for anything json can't handle. str turns it into its string form. Lossy but often fine.
json.dumps({"when":datetime.now()}, default=str)

# Pydantic handles this fine 

print("\n\nPydantic\n\n")

from pydantic import BaseModel

class Employee(BaseModel):
    name: str
    salary: int

emp = Employee(name="Ravi", salary=95000)

t = emp.model_dump()
print(t)
formatted = emp.model_dump_json(indent=2)
print(formatted)

# list of employees

employees = [Employee(name="Ravi", salary=95000), Employee(name="Anita", salary=82000)]

data = [e.model_dump() for e in employees]
print(data)
out_path.write_text(json.dumps(data, indent=2))