"""
Enumerate

Gives you the index and the item together, so you never index manually.
"""

items = ["a","b","c"]

for i, item in enumerate(items):
    print(f"{item} : {i}") # --- a:0, b:1, c:2

# Start counting from something other than zero:
for i, item in enumerate(items, start=1):
    print(f"{item} : {i}") # --- a:1, b:2, c:3

"""
zip

Walks two or more iterables in parallel, pairing them up.
"""

names = ["ravi", "anita", "suresh"]
scores = [88, 92, 71]

for name, score in zip(names, scores):
    print(name, score)


# make a dictionary
lookup = dict(zip(names, scores))
print(lookup) 

# if numbers do not match, it stops at the shortest, unless strict is used
names = ["ravi", "anita", "suresh"]
scores = [88, 92, 71, 90]

print(list(zip(names, scores))) # --- [('ravi', 88), ('anita', 92), ('suresh', 71)]

print(list(zip(names, scores, strict=True))) # -- ValueError: zip() argument 2 is longer than argument 1

