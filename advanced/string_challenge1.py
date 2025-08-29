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

# 3. Check if two strings are anagrams
def are_anagrams(s1, s2):
    return sorted(s1) == sorted(s2)
print("Are anagrams:", are_anagrams("listen", "silent"))  # Output: True

# 4. Find the first non-repeating character
def first_unique_char(s):
    from collections import Counter
    count = Counter(s)
    for c in s:
        if count[c] == 1:
            return c
    return None
print("First unique char:", first_unique_char("swiss"))  # Output: "w"


