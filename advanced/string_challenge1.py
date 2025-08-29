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


# 5. Longest substring without repeating characters
def length_of_longest_substring(s):
    char_index = {}
    left = max_len = 0
    for right, c in enumerate(s):
        if c in char_index and char_index[c] >= left:
            left = char_index[c] + 1
        char_index[c] = right
        max_len = max(max_len, right - left + 1)
    return max_len
print("Longest substring length:", length_of_longest_substring("abcabcbb"))  # Output: 3

# 6. String compression (e.g., "aabcccccaaa" -> "a2b1c5a3")
def compress_string(s):
    if not s:
        return ""
    result = []
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1]:
            count += 1
        else:
            result.append(s[i-1] + str(count))
            count = 1
    result.append(s[-1] + str(count))
    return ''.join(result)
print("Compressed string:", compress_string("aabcccccaaa"))  # Output: "a2b1c5a3"

# 7. Find all permutations of a string
def string_permutations(s):
    from itertools import permutations
    return set([''.join(p) for p in permutations(s)])
print("Permutations:", string_permutations("abc"))  # Output: {'abc', 'acb', 'bac', 'bca', 'cab', 'cba'}

# 8. Count vowels and consonants
def count_vowels_consonants(s):
    vowels = set('aeiouAEIOU')
    v = sum(1 for c in s if c in vowels)
    c = sum(1 for c in s if c.isalpha() and c not in vowels)
    return v, c
print("Vowels/Consonants:", count_vowels_consonants("Hello World!"))  # Output: (3, 7)

