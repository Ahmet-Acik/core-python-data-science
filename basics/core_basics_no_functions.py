from typing import Any 
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
from types import NoneType
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
    print(temp_file_content)
    

# 12. MODULES & IMPORTS
import math
from math import ceil
circle_area = math.pi * 2 ** 2
ceil_3_7 = ceil(3.7)


# 13. DECORATORS & GENERATORS (demonstrated without user-defined functions)
print('Running...')
say_hi_result = f"Hi, Streamlit!"
print('Done!')

countdown_gen = []
n = 3
while n > 0:
    countdown_gen.append(n)
    n -= 1
    
# 14. TYPE ANNOTATIONS (shown as comments)
score: int
gpa: float
fruits: list[str]
# person: dict[str, Any]
unique_fruits: set[str]
colors: tuple[str, ...]
nothing: NoneType

# person: dict[str, Any]  # type: ignore[no-redef]


# 15. REGEX & DATETIME
import re
from datetime import datetime, timedelta
text = "Conference 2025"
match = re.search(r'\b(20\d{2})\b', text)
extracted_year = match.group(1) if match else None

today = datetime.today()
next_week = today + timedelta(days=7)
week_range = (today.strftime('%Y-%m-%d'), next_week.strftime('%Y-%m-%d'))
print("This week:", week_range)


# 16. ARGPARSE (CLI) - not run, just shown
import argparse
parser = argparse.ArgumentParser(description='Demo CLI')
parser.add_argument('--repeat', type=int, default=2)
args = parser.parse_args([])  # Not using sys.argv for demo
cli_repeat = args.repeat


# 17. EXTENDED USAGE (DEMO OUTPUTS)
if __name__ == "__main__":
    print("--- Type Overview ---")
    print({
        'score': type(score),
        'gpa': type(gpa),
        'fruits': type(fruits),
        'person': type(person),
        'unique_fruits': type(unique_fruits),
        'colors': type(colors),
        'nothing': type(nothing)
    })

    print("\n--- Variables & Data Types ---")
    print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
    print(f"Score: {score}, GPA: {gpa}, Flag: {flag}, Nothing: {nothing}")

    print("\n--- Basic Operations ---")
    print(f"Total: {total}, Ratio: {ratio}, High score: {is_high_score}")

    print("\n--- Lists, Tuples, Sets, Dicts ---")
    print(f"Fruits: {fruits}, Colors: {colors}, Unique fruits: {unique_fruits}, Person: {person}")

    print("\n--- Control Flow ---")
    print(f"Result: {result}")
    print(f"First long word: {first_long_word}")
    print(f"Countdown: {countdown}")

    print("\n--- Lambdas & Expressions ---")
    print(greeted)
    print(f"Add 2+3: {added}")
    print(f"Square of 4: {squared}")

    print("\n--- Comprehensions ---")
    print(f"Lengths: {lengths}, Fruit map: {fruit_map}, First letters: {first_letters}")

    print("\n--- String/List/Dict Methods ---")
    print(f"Clean: {clean}, Words: {words}, Joined: {joined}, Replaced: {replaced}")
    print(f"Sorted nums: {nums}, Count of 2: {count_2}, Index of 9: {index_9}")

    print("\n--- Functional Tools ---")
    print(f"Evens: {evens}, Squares: {squares}, Product: {product}, All positive: {all_positive}, Any even: {any_even}")

    print("\n--- Exception Handling ---")
    print(f"Safe divide 10/2: {safe_divide_10_2}")
    print(f"Safe divide 10/0: {safe_divide_10_0}")

    print("\n--- File I/O & Context Managers ---")
    print(f"Temp file content: {temp_file_content}")

    print("\n--- Modules & Imports ---")
    print(f"Circle area (r=2): {circle_area}")
    print(f"Ceil 3.7: {ceil_3_7}")

    print("\n--- Decorators & Generators ---")
    print(say_hi_result)
    print(f"Countdown gen: {countdown_gen}")

    print("\n--- Regex & Datetime ---")
    print(f"Extract year: {extracted_year}")
    print(f"Week range: {week_range}")

    print("\n--- Argparse ---")
    print(f"CLI repeat: {cli_repeat}")