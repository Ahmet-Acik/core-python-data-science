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
