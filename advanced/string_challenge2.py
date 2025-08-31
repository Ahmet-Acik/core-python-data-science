"""
string_challenge2.py
--------------------
Advanced string challenges and Python string function practices.
Each challenge includes inline comments explaining what, where, and how.
"""

import string
import re
from collections import Counter

# 1. Find all words that are palindromes in a sentence
sentence = "Anna went to see civic duty at noon in the racecar"
words = sentence.split()  # Split sentence into words
palindromes = [w for w in words if w.lower() == w[::-1].lower()]
print("Palindromic words:", palindromes)  # ['Anna', 'civic', 'noon', 'racecar']


# 2. Capitalize the first letter of every word
text = "hello world! python is fun."
capitalized = text.title()  # Capitalizes first letter of each word
print("Title case:", capitalized)  # "Hello World! Python Is Fun."


# 3. Count the number of uppercase and lowercase letters
sample = "PyThOn Is AwEsOmE!"
upper_count = sum(1 for c in sample if c.isupper())
lower_count = sum(1 for c in sample if c.islower())
print("Uppercase:", upper_count, "Lowercase:", lower_count) # Output: Uppercase: 8 Lowercase: 7


# 4. Check if a string is a valid identifier
identifier = "my_var1"
is_valid = identifier.isidentifier()  # Checks Python identifier rules
print(f"'{identifier}' is valid identifier:", is_valid) # True


# 5. Remove all punctuation from a string
messy = "Hello, world! How's everything?"
no_punct = messy.translate(str.maketrans('', '', string.punctuation))
print("No punctuation:", no_punct)