"""
Path objects know they're paths.
They handle separators per-OS, and they carry methods instead of requiring a function call for everything.
"""

from pathlib import Path

HERE = Path(__file__)

print(HERE) # /Users/nkjith/Documents/Learning/python-ramp-up/python-week1/src/day04_pathlib/pathlibBasics.py

print(HERE.parent) # /Users/nkjith/Documents/Learning/python-ramp-up/python-week1/src/day04_pathlib

print(HERE.parent.parent)

## Inspecting a path

print("\n\nInspecting Path\n\n")

p : Path = HERE / "resources" / "employees.csv"

print(f"name - {p.name} \nwithout extension - {p.stem} \nExtension only - {p.suffix} \nParts - {p.parts} \nAbsolute Path - {p.absolute}")

# replace suffix

json_path = p.with_suffix(".json")
print(json_path)

# replace name
new_path = p.with_name("employees_clean.csv") # will return a new path, do not modify existing file name
print(new_path.name)

# FILE EXISTENCE

p.exists()      # does anything exist at this path
p.is_file()     # exists and is a file
p.is_dir()      # exists and is a directory

# Creating directories
out_dir = HERE.parent / "output"
out_dir.mkdir(parents=True, exist_ok=True)

print("\n\nFinding Files\n\n")

# Finding files
print(HERE)
csv_list = list(HERE.parent.glob("*.csv")) # empty as its inside another folder
print(csv_list)
csv_list = list(HERE.parent.rglob("*.csv")) # rglob will look recursively
print(csv_list)

def output_path(csv_path: Path) -> Path:
    out = csv_path.parent.parent / "output"
    out.mkdir(parents=True, exist_ok=True)
    print("\n\n")
    print(csv_path.with_suffix(".json"))
    return out / csv_path.with_suffix(".json").name


path_now = HERE.parent / "resources" / "employees.csv"
print(output_path(path_now))