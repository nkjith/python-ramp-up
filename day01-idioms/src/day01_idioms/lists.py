import random

print("\n\n")
print("normal list")
squares=[]
for n in range(10):
    squares.append(n*n)
print(squares)
print("\n\n")

print("maps")
TAX_RATE=0.8
prices = [1.09, 23.56, 57.84, 4.56, 6.78]
def calculate_total(base_price):
    return base_price + (base_price*TAX_RATE)


# map takes a function and iterable

total = map(calculate_total,prices)
print(list(total))
print("\n\n")

print("using list comprehension")
total_comp = [calculate_total(price) for price in prices]
print(total_comp)
print("\n\n")

print("using list comprehension with conditionals")
cubes = [n*n*n for n in range(10) if n % 2 == 0]
print(cubes)
print("\n\n")


# filters value using function
print("filters value using function")
sentence = (
   "The rocket, who was named Ted, came back "
   "from Mars because he missed his friends."
)

def is_consonant(letter):
    vowels = "aeiou"
    return letter.isalpha() and letter.lower() not in vowels

consonants = [char for char in sentence if is_consonant(char)]
print(consonants)
print("\n\n")

# Sets to remove duplicates - Use braces instead of square brackets
print("Using sets")
consonant_set={char for char in sentence if is_consonant(char)}
print(consonant_set)
print("\n\n")

# Dictionary -- Use braces instead of square brackets
print("Using Dictionary")
squares_dict = {number: number * number for number in range(10)}
print(squares_dict)
print("\n\n")

# Nested lists
print("Nested lists")
def get_weather_data():
    return random.randrange(90, 110)

cities = ["Austin", "Tacoma", "Topeka", "Sacramento", "Charlotte"]

temperature_data = {city: [get_weather_data() for _ in range(7)] for city in cities}
print(temperature_data)
print("\n\n")

# Prints 7 randoms
print([get_weather_data() for _ in range(7)])
