
"""
core_basics.py
----------------
A step-by-step, beginner-friendly introduction to Python for data science, scripting, and automation.

This file follows a progressive pedagogy:
    1. Variables & assignment
    2. Data types (numbers, strings, booleans, None)
    3. Basic operations
    4. Lists, tuples, sets, dictionaries
    5. Control flow (if, for, while)
    6. Functions & lambdas
    7. Comprehensions
    8. String/list/dict methods
    9. Functional tools (map, filter, reduce, any, all)
    10. Exception handling
    11. File I/O & context managers
    12. Modules & imports
    13. Decorators & generators
    14. Type annotations
    15. Regex & datetime
    16. Argparse (CLI)
    17. Extended usage
"""

from typing import Generator, Callable
from functools import reduce
import math
from math import ceil
from contextlib import contextmanager
import re
from datetime import datetime, timedelta
import argparse


from typing import Generator, Callable



# 1. VARIABLES & ASSIGNMENT
age = 21
height = 1.68
name = "Mina"
is_student = True

# 2. DATA TYPES
score = 95            # int
gpa = 3.87            # float
greeting = "Hello!"   # str
flag = False          # bool
nothing = None        # NoneType

# 3. BASIC OPERATIONS
total = score + 5
ratio = gpa / 4
is_high_score = score > 90

# 4. LISTS, TUPLES, SETS, DICTS
fruits = ["apple", "banana", "kiwi"] # List
fruits.append("pear")
colors = ("red", "green", "blue") # Tuple
unique_fruits = {"apple", "banana", "apple"} # Set
person = {"name": name, "age": age} # Dict
person["city"] = "Bursa"

# 5. CONTROL FLOW
if is_high_score:
    result = "Excellent"
elif score > 70:
    result = "Good"
else:
    result = "Needs improvement"

for fruit in fruits:
    pass

def find_first_long_word(words: list[str], min_len: int) -> str | None:
    for w in words:
        if len(w) >= min_len:
            return w
    return None

def count_down(n: int) -> list[int]:
    out = []
    while n > 0:
        out.append(n)
        n -= 1
    return out

# 6. FUNCTIONS & LAMBDAS
def greet(name: str) -> str:
    return f"Hi, {name}!"

def add(a: float, b: float = 0) -> float:
    return a + b

square = lambda x: x * x

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

# 9. FUNCTIONAL TOOLS
evens = list(filter(lambda x: x % 2 == 0, nums))
squares = list(map(lambda x: x**2, nums))
product = reduce(lambda x, y: x * y, nums)
all_positive = all(x > 0 for x in nums)
any_even = any(x % 2 == 0 for x in nums)

# 10. EXCEPTION HANDLING
def safe_divide(a: float, b: float) -> float | str:
    try:
        return a / b
    except ZeroDivisionError:
        return 'Cannot divide by zero'

class CustomError(Exception):
    pass

# 11. FILE I/O & CONTEXT MANAGERS
@contextmanager
def open_temp_file():
    f = open('tempfile.txt', 'w')
    try:
        yield f
    finally:
        f.close()

def write_and_read_temp() -> str:
    with open_temp_file() as f:
        f.write('Temporary data!')
    with open('tempfile.txt', 'r') as f:
        return f.read()

# 12. MODULES & IMPORTS
circle_area = lambda r: math.pi * r ** 2
ceil_3_7 = ceil(3.7)

# 13. DECORATORS & GENERATORS
def announce(func):
    def wrapper(*args, **kwargs):
        print('Running...')
        result = func(*args, **kwargs)
        print('Done!')
        return result
    return wrapper

@announce
def say_hi(name: str) -> str:
    return f"Hi, {name}!"

def countdown_gen(n: int) -> Generator[int, None, None]:
    while n > 0:
        yield n
        n -= 1

# 14. TYPE ANNOTATIONS
def type_overview() -> dict[str, type]:
    return {
        'score': type(score),
        'gpa': type(gpa),
        'fruits': type(fruits),
        'person': type(person),
        'unique_fruits': type(unique_fruits),
        'colors': type(colors),
        'nothing': type(nothing)
    }

# 15. REGEX & DATETIME
def extract_year(text: str) -> str | None:
    match = re.search(r'\b(20\d{2})\b', text)
    return match.group(1) if match else None

def week_range() -> tuple[str, str]:
    today = datetime.today()
    next_week = today + timedelta(days=7)
    return today.strftime('%Y-%m-%d'), next_week.strftime('%Y-%m-%d')

# 16. ARGPARSE (CLI)
def parse_cli() -> int:
    parser = argparse.ArgumentParser(description='Demo CLI')
    parser.add_argument('--repeat', type=int, default=2)
    args = parser.parse_args([])
    return args.repeat

# 17. EXTENDED USAGE
if __name__ == "__main__":
    print("--- Type Overview ---")
    print(type_overview())

    print("\n--- Variables & Data Types ---")
    print(f"Name: {name}, Age: {age}, Height: {height}, Student: {is_student}")
    print(f"Score: {score}, GPA: {gpa}, Flag: {flag}, Nothing: {nothing}")

    print("\n--- Basic Operations ---")
    print(f"Total: {total}, Ratio: {ratio}, High score: {is_high_score}")

    print("\n--- Lists, Tuples, Sets, Dicts ---")
    print(f"Fruits: {fruits}, Colors: {colors}, Unique fruits: {unique_fruits}, Person: {person}")

    print("\n--- Control Flow ---")
    print(f"Result: {result}")
    print(f"First long word: {find_first_long_word(fruits, 5)}")
    print(f"Countdown: {count_down(3)}")

    print("\n--- Functions & Lambdas ---")
    print(greet("Ada"))
    print(f"Add 2+3: {add(2,3)}")
    print(f"Square of 4: {square(4)}")

    print("\n--- Comprehensions ---")
    print(f"Lengths: {lengths}, Fruit map: {fruit_map}, First letters: {first_letters}")

    print("\n--- String/List/Dict Methods ---")
    print(f"Clean: {clean}, Words: {words}, Joined: {joined}, Replaced: {replaced}")
    print(f"Sorted nums: {nums}, Count of 2: {count_2}, Index of 9: {index_9}")

    print("\n--- Functional Tools ---")
    print(f"Evens: {evens}, Squares: {squares}, Product: {product}, All positive: {all_positive}, Any even: {any_even}")

    print("\n--- Exception Handling ---")
    print(f"Safe divide 10/2: {safe_divide(10,2)}")
    print(f"Safe divide 10/0: {safe_divide(10,0)}")

    print("\n--- File I/O & Context Managers ---")
    print(f"Temp file content: {write_and_read_temp()}")

    print("\n--- Modules & Imports ---")
    print(f"Circle area (r=2): {circle_area(2)}")
    print(f"Ceil 3.7: {ceil_3_7}")

    print("\n--- Decorators & Generators ---")
    print(say_hi("Streamlit"))
    print(f"Countdown gen: {list(countdown_gen(3))}")

    print("\n--- Regex & Datetime ---")
    print(f"Extract year: {extract_year('Conference 2025')}")
    print(f"Week range: {week_range()}")

    print("\n--- Argparse ---")
    print(f"CLI repeat: {parse_cli()}")

# =========================
# DATA TYPES & STRUCTURES
# =========================
# Numbers
unit_price = 8.50
units = 5
total_cost = unit_price * units

# Strings
country = "Turkey"
user_name = "Ada"
welcome = f"Welcome, {user_name} from {country}!"
upper_country = country.upper()

# Lists
scores = [88, 92, 79, 85]
scores.append(90)
avg_score = sum(scores) / len(scores)

# Tuples
rgb_color = (128, 64, 255)
today = (2025, 8, 18)

# Dictionaries
user_age = 28
employee = {"name": user_name, "age": user_age, "city": country}
employee["role"] = "Analyst"
for k, v in employee.items():
    pass

# Sets
tech_stack = {"python", "sql", "numpy", "python"}
tech_stack.add("pandas")

# NoneType
maybe_value = None

# Useful built-ins
max_score = max(scores)
min_score = min(scores)
unique_stack = list(set(tech_stack))
rounded_cost = round(unit_price)
enum_scores = list(enumerate(scores))
score_pairs = list(zip(scores, range(len(scores))))

# =========================
# COMPREHENSIONS
# =========================
# List comprehension
km = [round(miles * 1.609, 2) for miles in [1, 5, 10, 26.2]]
# Dict comprehension
city_lengths = {city: len(city) for city in ["Paris", "Berlin", "Rome"]}
# Set comprehension
first_letters = {city[0] for city in ["Paris", "Berlin", "Rome", "Prague"]}

# =========================
# LOOPS
# =========================
for idx, score in enumerate(scores):
    pass

for s, day in zip(scores, ["Mon", "Tue", "Wed", "Thu", "Fri"]):
    pass

def first_below(scores: list[int], threshold: int) -> int | None:
    """
    Return the first score below the threshold.
    """
    i = 0
    while i < len(scores):
        if scores[i] < threshold:
            return scores[i]
        i += 1
    return None

# =========================
# STRING METHODS
# =========================
phrase = "  Data is powerful!  "
trimmed = phrase.strip()
words = trimmed.split()
joined = ":".join(words)
replaced = trimmed.replace("powerful", "fun")
is_title = trimmed.istitle()
upper = trimmed.upper()
lower = trimmed.lower()

# =========================
# LIST METHODS
# =========================
nums = [8, 3, 5, 3, 9, 2]
nums.sort()
nums.reverse()
nums.append(7)
nums.remove(3)
count_3 = nums.count(3)
index_5 = nums.index(5) if 5 in nums else -1

# =========================
# FUNCTIONAL PROGRAMMING
# =========================
evens = list(filter(lambda x: x % 2 == 0, nums))
squares = list(map(lambda x: x**2, nums))
from functools import reduce
product = reduce(lambda x, y: x * y, nums)
all_positive = all(x > 0 for x in nums)
any_even = any(x % 2 == 0 for x in nums)

# =========================
# DATA TYPES
# =========================
# Built-in types: int, float, str, bool, list, tuple, dict, set, NoneType

integer = 17
floating = 3.1415
complex_num = 1 + 2j
list_comp = [x + 1 for x in range(4)]
dict_comp = {x: x + 1 for x in range(4)}
set_comp = {x % 3 for x in range(6)}

# =========================
# LAMBDA & FUNCTIONAL TOOLS
# =========================
nums2 = [2, 4, 6, 8]
squares2 = list(map(lambda x: x**2, nums2))
evens2 = list(filter(lambda x: x % 2 == 0, nums2))
product2 = reduce(lambda x, y: x * y, nums2)
pairs2 = list(zip(nums2, squares2))

# =========================
# EXCEPTION HANDLING
# =========================
def safe_div(a: float, b: float) -> float | str:
    """
    Divide a by b, handling division by zero.
    """
    try:
        return a / b
    except ZeroDivisionError:
        return 'Zero division error'
    finally:
        pass

class DataError(Exception):
    """Custom exception for demonstration."""
    pass

# =========================
# FILE I/O
# =========================
def write_and_read() -> str:
    """
    Write a string to a file and read it back.
    """
    with open('demo.txt', 'w') as f:
        f.write('Sample file!')
    with open('demo.txt', 'r') as f:
        return f.read()

# =========================
# MODULES & PACKAGES
# =========================
import math
from math import sqrt
pi_val = math.pi
sqrt_25 = sqrt(25)

# =========================
# DECORATORS & GENERATORS
# =========================
def log_decorator(func):
    """
    Print before and after calling the function.
    """
    def wrapper(*args, **kwargs):
        print('Start')
        result = func(*args, **kwargs)
        print('End')
        return result
    return wrapper

@log_decorator
def greet_user(name: str) -> str:
    return f"Hello, {name}!"

def count_up() -> Generator[int, None, None]:
    for i in range(3):
        yield i

# =========================
# TYPE ANNOTATIONS
# =========================
def add_nums(a: int, b: int) -> int:
    return a + b
x_typed: float = 2.71
y_typed: str = 'hi'

# =========================
# CONTEXT MANAGERS
# =========================
from contextlib import contextmanager
@contextmanager
def open_resource():
    print('Resource opened')
    yield 'resource'
    print('Resource closed')

# =========================
# REGULAR EXPRESSIONS
# =========================
import re
def regex_demo() -> tuple[list[str], list[str], str]:
    text = 'Python 2025!'
    numbers = re.findall(r'\d+', text)
    words = re.findall(r'\w+', text)
    replaced = re.sub(r'\d+', 'YEAR', text)
    return numbers, words, replaced

# =========================
# DATETIME
# =========================
from datetime import datetime, timedelta
def datetime_demo() -> tuple[datetime, datetime, str]:
    now = datetime.now()
    next_week = now + timedelta(days=7)
    formatted = now.strftime('%d-%m-%Y')
    return now, next_week, formatted

# =========================
# ARGPARSE
# =========================
import argparse
def cli_example() -> int:
    parser = argparse.ArgumentParser(description='Demo')
    parser.add_argument('--val', type=int, default=10)
    args = parser.parse_args([])
    return args.val

# Strings
single = 'single'
double = "double"
multiline = """multi\nline\ntext"""

# Boolean
flag = True

# Lists
cities = ['Paris', 'Berlin', 'Rome']
cities.append('Prague')

# Tuples
point = (5, 9)

# Dictionaries
person = {'name': 'Deniz', 'age': 28}
person['city'] = 'Izmir'

# Sets
unique_vals = {1, 2, 3, 2}

# NoneType
nothing = None

def type_demo() -> tuple[type, ...]:
    str_var = "demo"
    return type(integer), type(floating), type(str_var), type(cities), type(person), type(unique_vals), type(nothing)

# =========================
# CONTROL FLOW
# =========================
def number_sign(x: float) -> str:
    if x > 0:
        return "Positive"
    elif x < 0:
        return "Negative"
    else:
        return "Zero"

def sum_numbers(lst: list[float]) -> float:
    total = 0
    for item in lst:
        total += item
    return total

def countdown_list(n: int) -> list[int]:
    result = []
    while n > 0:
        result.append(n)
        n -= 1
    return result

def first_even_num(nums: list[int]) -> int | None:
    for n in nums:
        if n % 2 == 0:
            return n
    return None

# =========================
# FUNCTIONS
# =========================
def hello(name: str) -> str:
    return f"Hi, {name}!"

def add_floats(a: float, b: float = 0) -> float:
    return a + b

def sum_args(*args: float) -> float:
    return sum(args)

def info_str(**kwargs) -> str:
    return ', '.join(f"{k}={v}" for k, v in kwargs.items())

square = lambda x: x * x

def make_adder(x: int) -> Callable[[int], int]:
    def inner(y: int) -> int:
        return x + y
    return inner

# =========================
# EXTENDED EXAMPLE USAGE
# =========================
if __name__ == "__main__":
    print("--- Type Demo ---")
    print(type_demo())

    print("\n--- Control Flow ---")
    print("Sign of -3:", number_sign(-3))
    print("Sum of [2,4,6]:", sum_numbers([2,4,6]))
    print("Countdown from 4:", countdown_list(4))
    print("First even in [1,5,7,10]:", first_even_num([1,5,7,10]))

    print("\n--- Functions ---")
    print(hello("Ada"))
    print("Add 3+4:", add_floats(3,4))
    print("Sum args 2,3,4:", sum_args(2,3,4))
    print("Info str:", info_str(name="Deniz", age=28))
    print("Square of 5:", square(5))
    print("Adder 7+2:", make_adder(7)(2))

    print("\n--- Comprehensions ---")
    print("KM:", km)
    print("City lengths:", city_lengths)
    print("First letters:", first_letters)

    print("\n--- String & List Methods ---")
    print("Trimmed phrase:", trimmed)
    print("Words:", words)
    print("Joined:", joined)
    print("Replaced:", replaced)
    print("Upper:", upper)
    print("Sorted nums:", nums)
    print("Count of 3:", count_3)
    print("Index of 5:", index_5)

    print("\n--- Functional Programming ---")
    print("Evens:", evens)
    print("Squares:", squares)
    print("Product:", product)
    print("All positive:", all_positive)
    print("Any even:", any_even)

    print("\n--- Exception Handling ---")
    print("Safe div 8/2:", safe_div(8,2))
    print("Safe div 8/0:", safe_div(8,0))

    print("\n--- File I/O ---")
    print("File content:", write_and_read())

    print("\n--- Modules & Packages ---")
    print("Pi:", pi_val)
    print("Sqrt 25:", sqrt_25)

    print("\n--- Decorators & Generators ---")
    print(greet_user("Streamlit"))
    print("Generator output:", list(count_up()))

    print("\n--- Type Annotations ---")
    print("Add nums 2+5:", add_nums(2,5))

    print("\n--- Context Managers ---")
    with open_resource() as val:
        print("Inside context:", val)

    print("\n--- Regex ---")
    print("Regex demo:", regex_demo())

    print("\n--- Datetime ---")
    print("Datetime demo:", datetime_demo())

    print("\n--- Argparse ---")
    print("CLI example:", cli_example())
