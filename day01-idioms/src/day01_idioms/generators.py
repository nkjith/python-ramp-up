"""
A generator produces values one at a time, on demand, instead of building the whole collection up front in memory.

**`open(file_name)` is already lazy, on its own.** A file object in Python doesn't read the whole file into memory when you open it — it's an iterator over lines.

There are generator functions and generator expressions
"""
from pathlib import Path

HERE = Path(__file__).parent
csv_path = HERE / "resources" / "employees.csv"

# open(file_name) is already lazy, on its own. 
# A file object in Python doesn't read the whole file into memory when you open it — it's an iterator over lines

# Generator EXPRESSION — no function involved at all
csv_gen = (row for row in open(csv_path))
for row in csv_gen:
   print(row.strip())

print(csv_gen) # --- <generator object <genexpr> at 0x109723cf0>
print(type(csv_gen)) # --- <class 'generator'>

# Generator FUNCTION — this one uses yield, IS a function
def read_lines(path):
   with open(path) as file:
    for row in file:  # noqa: UP028
        yield row

print(type(read_lines)) # --- function

generated_lines = read_lines(csv_path)

print(type(generated_lines)) # --- <class 'generator'>

for row in generated_lines:
  print(row)

print("printing again **********")
# nothing left — empty, prints nothing --- generator only gives one trip. 
for row in generated_lines:
  print(row)


""" Learning Yield 

return exits the function completely. Call it again, it starts fresh from line 1. The function has no memory between calls.

yield is different: it pauses instead of exiting

"""

def count_up():
    print("starting")
    yield 1
    print("got here after first yield")
    yield 2
    print("got here after second yield")
    yield 3
    print("done")

# print only generator object type, not calling the function yet.
# Think of it as a paused, ready-to-run version of the function, sitting at the very top, waiting.
count = count_up()
print(count) # --- <generator object count_up at 0x105c18ac0>

next(count) # --- starting And it returns 1. 
# The function ran from the top, hit yield 1, handed out 1, and froze exactly there — mid-function, with all its local variables still intact.

next(count) # --- got here after first yield. Returns 2 and froze

next(count) # --- got here after second yield. Returns 3 and froze

#next(count) # done, Then raises StopIteration — there's no more yield left, the function fell off the end.

print("\n\nPrinting whole function\n\n")

"""
starting
1
got here after first yield
2
got here after second yield
3
done
"""
new_counter = count_up()
for item in new_counter:
   print(item)


# APPLYING TO READ FILE

def file_reader(path):
   with open(path) as file:
      for row in file:  # noqa: UP028
         yield row

reader = file_reader(csv_path)

for line in reader:
   print(line)


"""
WHY USE GENERATOR 


The one that actually matters for your AI work: memory, on a file too big to fit in RAM
Imagine employees.csv has 50 million rows instead of 10.

# Non-generator version — loads ALL 50 million lines into a list, in memory, at once
def file_reader_bad(path):
    with open(path) as file:
        return [row.strip() for row in file]   # returns a full list

lines = file_reader_bad("huge_file.csv")   # could crash your program — tries to hold everything


# Generator version — never holds more than ONE line in memory at a time
def file_reader(path):
    with open(path) as file:
        for row in file:
            yield row.strip()

for line in file_reader("huge_file.csv"):   # processes one line, discards it, gets the next
    process(line)
"""