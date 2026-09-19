"""
In Python there is sort and sorted
sort() sorts the existing structure
sorted() create a new list 
"""

num = [5,3,7,1,10,100,2]
num.sort()
print(num) # --- default sorting is ascending

# To sort descending
num.sort(reverse=True)
print(num) # --- descending

# Sorted
numbers = [45,23,67,12,68,100]
sorted_list = sorted(numbers)
print(sorted_list)

desc_list = sorted(numbers, reverse=True)
print(desc_list)


# Sort using a key
sample_dict = {"Alaska": 100, "Delhi": 45, "Kerala": 34}

items = list(sample_dict.items())

items.sort(key=lambda x: x[1])

print(items)

# Reverse 

items.sort(key=lambda x:x[1], reverse=True)

print(items)