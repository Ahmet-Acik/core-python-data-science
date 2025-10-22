"""
string_challenge3.py
--------------------
Advanced string challenges: regex, formatting, encoding, similarity, tokenization, normalization, substring search, efficient manipulation, and real-world parsing.
Each section includes explanations and sample outputs.
"""

import re
import base64
import unicodedata
from difflib import SequenceMatcher
from io import StringIO
import json

# 1. Extract emails, dates, and phone numbers using regex
text = "Contact: alice@example.com, bob@work.org. Date: 2025-10-22. Phone: +1-555-123-4567"
emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
phones = re.findall(r"\+\d-\d{3}-\d{3}-\d{4}", text)
print("Emails:", emails)  # ['alice@example.com', 'bob@work.org']
print("Dates:", dates)    # ['2025-10-22']
print("Phones:", phones) # ['+1-555-123-4567']

# 2. String formatting: f-strings, format(), alignment, precision
name = "Ada"
score = 98.7654
print(f"Hello, {name}! Your score is {score:.2f}.")  # f-string with 2 decimals
print("Name: {:<10} | Score: {:>7.1f}".format(name, score))  # alignment

# 3. Encoding/decoding: base64, utf-8
original = "Python 🐍"
utf8_bytes = original.encode('utf-8')
b64 = base64.b64encode(utf8_bytes)
decoded = base64.b64decode(b64).decode('utf-8')
print("Base64:", b64)
print("Decoded:", decoded)

# 4. Multilingual/unicode handling
accented = "Café naïve résumé"
normalized = unicodedata.normalize('NFKD', accented)
ascii_only = normalized.encode('ascii', 'ignore').decode('ascii')
print("ASCII only:", ascii_only)  # 'Cafe naive resume'

# 5. String similarity: Levenshtein (difflib), Jaccard
def jaccard_similarity(s1, s2):
	set1, set2 = set(s1), set(s2)
	return len(set1 & set2) / len(set1 | set2)
sim = SequenceMatcher(None, "kitten", "sitting").ratio()
jaccard = jaccard_similarity("night", "nacht")
print("Levenshtein ratio:", sim)
print("Jaccard similarity:", jaccard)

# 6. Tokenization: split by regex, word boundaries
sentence = "Hello, world! This is a test."
tokens = re.findall(r"\b\w+\b", sentence)
print("Tokens:", tokens)

# 7. Text normalization: lowercase, stemming, lemmatization (basic)
raw = "Running runs runner"
lower = raw.lower()
stemmed = [w.rstrip('ing').rstrip('s') for w in lower.split()]  # crude stem
print("Lowercase:", lower)
print("Stemmed:", stemmed)

# 8. Substring search: Knuth-Morris-Pratt (KMP) algorithm
def kmp_search(text, pattern):
	# Preprocess pattern
	lps = [0]*len(pattern)
	j = 0
	for i in range(1, len(pattern)):
		while j > 0 and pattern[i] != pattern[j]:
			j = lps[j-1]
		if pattern[i] == pattern[j]:
			j += 1
			lps[i] = j
	# Search
	result = []
	j = 0
	for i in range(len(text)):
		while j > 0 and text[i] != pattern[j]:
			j = lps[j-1]
		if text[i] == pattern[j]:
			j += 1
		if j == len(pattern):
			result.append(i-j+1)
			j = lps[j-1]
	return result
print("KMP search indices:", kmp_search("ababcabcabababd", "ababd"))  # [10]

# 9. Efficient large string manipulation: StringIO, join vs concat
parts = ["data"] * 10000
joined = ''.join(parts)
buffer = StringIO()
for part in parts:
	buffer.write(part)
result = buffer.getvalue()
print("Join == StringIO:", joined == result)

# 10. Real-world parsing: CSV, log lines, JSON in string
csv_line = "name,age,city\nAda,21,London\nBob,30,Paris"
rows = [row.split(',') for row in csv_line.split('\n')]
print("CSV rows:", rows)

log_line = "2025-10-22 10:00:00 INFO User logged in"
date, time, level, *msg = log_line.split()
print("Log parsed:", date, time, level, ' '.join(msg))

json_str = '{"name": "Ada", "age": 21, "city": "London"}'
parsed = json.loads(json_str)
print("JSON parsed:", parsed)
