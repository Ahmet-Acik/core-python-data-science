"""
core_basics_no_functions.py
---------------------------
A beginner-friendly, step-by-step introduction to Python for data science, scripting, and automation.
This version demonstrates all concepts directly, without using user-defined functions.
"""

# 1. VARIABLES & ASSIGNMENT
age = 21
height = 1.68
name = "Mina"
is_student = True


# 2. DATA TYPES
score = 95
gpa = 3.87
greeting = "Hello!"
flag = False
nothing = None


# 3. BASIC OPERATIONS
total = score + 5
ratio = gpa / 4
is_high_score = score > 90

# 4. LISTS, TUPLES, SETS, DICTS
fruits = ["apple", "banana", "kiwi"]
fruits.append("pear")
colors = ("red", "green", "blue")
unique_fruits = {"apple", "banana", "apple"}
person = {"name": name, "age": age}
person["city"] = "Bursa"


# 5. CONTROL FLOW
if is_high_score:
    result = "Excellent"
elif score > 70:
    result = "Good"
else:
    result = "Needs improvement"

first_long_word = None
for w in fruits:
    if len(w) >= 5:
        first_long_word = w
        break

countdown = []
n = 3
while n > 0:
    countdown.append(n)
    n -= 1


# 6. LAMBDAS & SIMPLE EXPRESSIONS
greeted = f"Hi, {name}!"
added = 2 + 3
squared = (lambda x: x * x)(4)


# 7. COMPREHENSIONS
lengths = [len(f) for f in fruits]
fruit_map = {f: len(f) for f in fruits}
first_letters = {f[0] for f in fruits}


# 8. STRING/LIST/DICT METHODS
sentence = "  Python is fun!  "
clean = sentence.strip()
words = clean.split()
joined = ",".join(words)
replaced = clean.replace("fun", "awesome")
nums = [5, 2, 9, 2]
nums.sort()
nums.append(7)
nums.remove(2)
count_2 = nums.count(2)
index_9 = nums.index(9) if 9 in nums else -1
person_keys = list(person.keys())
person_values = list(person.values())



# 9. FUNCTIONAL TOOLS
from functools import reduce
evens = list(filter(lambda x: x % 2 == 0, nums))
squares = list(map(lambda x: x**2, nums))
product = reduce(lambda x, y: x * y, nums)
all_positive = all(x > 0 for x in nums)
any_even = any(x % 2 == 0 for x in nums)
zipped = list(zip(fruits, colors))


# 10. EXCEPTION HANDLING
try:
    safe_divide_10_2 = 10 / 2
except ZeroDivisionError:
    safe_divide_10_2 = 'Cannot divide by zero'

try:
    safe_divide_10_0 = 10 / 0
except ZeroDivisionError:
    safe_divide_10_0 = 'Cannot divide by zero'


# 11. FILE I/O & CONTEXT MANAGERS
with open('tempfile.txt', 'w') as f:
    f.write('Temporary data!')
with open('tempfile.txt', 'r') as f:
    temp_file_content = f.read()