"""
string_challenge1.py
--------------------
Most common string coding questions and answers for SDET interviews.
"""

# 1. Reverse a string
def reverse_string(s):
    return s[::-1]
print("Reverse:", reverse_string("hello"))  # Output: "olleh"

# 2. Check if a string is a palindrome
def is_palindrome(s):
    return s == s[::-1]
print("Is palindrome:", is_palindrome("racecar"))  # Output: True

