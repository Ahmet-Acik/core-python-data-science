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

# 6. Replace multiple spaces with a single space
messy_spaces = "This   is   a    test."
single_spaced = ' '.join(messy_spaces.split())  # Splits and rejoins to remove extra spaces
print("Single spaced:", single_spaced) # 


# 7. Find the longest word in a sentence
sentence2 = "Python programming is both fun and educational"
longest = max(sentence2.split(), key=len)
print("Longest word:", longest)  # "programming"

# 8. Check if all characters in a string are unique
unique_str = "abcdefg"
is_unique = len(set(unique_str)) == len(unique_str)
print("All unique characters:", is_unique)


# 9. Find all substrings of length k
s = "abcdef"
k = 3
substrings_k = [s[i:i+k] for i in range(len(s)-k+1)]
print(f"All substrings of length {k}:", substrings_k)


# 10. Group anagrams from a list of words
word_list = ["listen", "silent", "enlist", "google", "gooegl", "cat", "tac"]
anagram_groups = {}
for word in word_list:
    key = tuple(sorted(word))  # Sort letters to form a key
    anagram_groups.setdefault(key, []).append(word)
print("Anagram groups:", list(anagram_groups.values()))


# 11. Check if a string contains only printable characters
test_str = "Hello\nWorld"
print("Is printable:", test_str.isprintable())  # False due to \n


# 12. Reverse the order of words in a sentence
sentence3 = "the quick brown fox"
reversed_words = ' '.join(sentence3.split()[::-1])
print("Words reversed:", reversed_words)


# 13. Find the most common word in a paragraph
paragraph = "dog cat dog bird cat dog"
words = paragraph.lower().split()
most_common_word, count = Counter(words).most_common(1)[0]
print("Most common word:", most_common_word, "Count:", count)


# 14. Check if a string is a valid email address (simple regex)
email = "test.user@example.com"
is_email = bool(re.match(r"^[\w\.-]+@[\w\.-]+\.\w+$", email))
print("Is valid email:", is_email)


# 15. Count the number of digits, letters, and special characters
mixed = "abc123!@#"
digits = sum(c.isdigit() for c in mixed)
letters = sum(c.isalpha() for c in mixed)
specials = sum(not c.isalnum() for c in mixed)
print("Digits:", digits, "Letters:", letters, "Specials:", specials)


# 16. Find all start indices of a substring in a string
haystack = "abracadabra"
needle = "abra"
indices = [i for i in range(len(haystack)) if haystack.startswith(needle, i)]
print("Start indices of 'abra':", indices)


# 17. Remove leading and trailing whitespace and newlines
messy2 = "   \n\tHello, World!  \n"
cleaned = messy2.strip()
print("Stripped string:", repr(cleaned)) 


# 18. Swap case of all letters
swap = "PyThOn"
swapped = swap.swapcase()
print("Swapcase:", swapped)  # "pYtHoN"


# 19. Center a string with padding
centered = "Python".center(20, '*')
print("Centered:", centered)


# 20. Split a string into lines
multiline = "Line1\nLine2\nLine3"
lines = multiline.splitlines()
print("Lines:", lines)


# 21. Check if a string is numeric (integer or float)
num_str1 = "12345"
num_str2 = "12.345"
is_num1 = num_str1.isdigit()
is_num2 = num_str2.replace('.', '', 1).isdigit() and num_str2.count('.') < 2
print("Is integer:", is_num1, "Is float-like:", is_num2)


# 22. Pad a string with zeros (left)
padded = "42".zfill(5)
print("Zero padded:", padded)


# 23. Remove a prefix or suffix (Python 3.9+)
filename = "data_report.csv"
if hasattr(filename, "removesuffix"):
    print("Without suffix:", filename.removesuffix(".csv"))
    print("Without prefix:", filename.removeprefix("data_"))
else:
    print("Remove prefix/suffix not supported.")
    

# 24. Find all numbers in a string
text_with_numbers = "Order 66 was issued in year 19BBY, cost: $500"
numbers = re.findall(r'\d+', text_with_numbers)
print("Numbers found:", numbers)


# 25. Join a list of strings with a custom separator
parts = ["2023", "08", "31"]
date_str = "-".join(parts)
print("Joined date:", date_str)