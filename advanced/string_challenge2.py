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
