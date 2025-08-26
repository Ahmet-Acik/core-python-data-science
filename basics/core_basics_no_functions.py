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