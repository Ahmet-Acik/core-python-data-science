import unittest
import re
import base64
import unicodedata
from difflib import SequenceMatcher
from io import StringIO
import json
from advanced import string_challenge3 as sc3

class TestStringChallenge3(unittest.TestCase):
    def test_regex_extraction(self):
        text = "Contact: alice@example.com, bob@work.org. Date: 2025-10-22. Phone: +1-555-123-4567"
        emails = re.findall(r"[\w\.-]+@[\w\.-]+", text)
        dates = re.findall(r"\d{4}-\d{2}-\d{2}", text)
        phones = re.findall(r"\+\d-\d{3}-\d{3}-\d{4}", text)
        self.assertIn("alice@example.com", emails)
        self.assertIn("2025-10-22", dates)
        self.assertIn("+1-555-123-4567", phones)

    def test_string_formatting(self):
        name = "Ada"
        score = 98.7654
        self.assertEqual(f"Hello, {name}! Your score is {score:.2f}.", "Hello, Ada! Your score is 98.77.")
        self.assertEqual("Name: {:<10} | Score: {:>7.1f}".format(name, score), "Name: Ada        | Score:    98.8")

    def test_encoding_decoding(self):
        original = "Python 🐍"
        utf8_bytes = original.encode('utf-8')
        b64 = base64.b64encode(utf8_bytes)
        decoded = base64.b64decode(b64).decode('utf-8')
        self.assertEqual(decoded, original)

    def test_unicode_handling(self):
        accented = "Café naïve résumé"
        normalized = unicodedata.normalize('NFKD', accented)
        ascii_only = normalized.encode('ascii', 'ignore').decode('ascii')
        self.assertEqual(ascii_only, "Cafe naive resume")

    def test_string_similarity(self):
        sim = SequenceMatcher(None, "kitten", "sitting").ratio()
        self.assertGreater(sim, 0.5)
        def jaccard_similarity(s1, s2):
            set1, set2 = set(s1), set(s2)
            return len(set1 & set2) / len(set1 | set2)
        jaccard = jaccard_similarity("night", "nacht")
        self.assertGreaterEqual(jaccard, 0)
        self.assertLessEqual(jaccard, 1)

    def test_tokenization(self):
        sentence = "Hello, world! This is a test."
        tokens = re.findall(r"\b\w+\b", sentence)
        self.assertIn("Hello", tokens)
        self.assertIn("world", tokens)
        self.assertEqual(len(tokens), 6)

    def test_text_normalization(self):
        raw = "Running runs runner"
        lower = raw.lower()
        stemmed = [w.rstrip('ing').rstrip('s') for w in lower.split()]
        self.assertEqual(lower, "running runs runner")
        self.assertEqual(stemmed[0], "ru")

    def test_kmp_search(self):
        def kmp_search(text, pattern):
            lps = [0]*len(pattern)
            j = 0
            for i in range(1, len(pattern)):
                while j > 0 and pattern[i] != pattern[j]:
                    j = lps[j-1]
                if pattern[i] == pattern[j]:
                    j += 1
                    lps[i] = j
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
        indices = kmp_search("ababcabcabababd", "ababd")
        self.assertEqual(indices, [10])

    def test_stringio_vs_join(self):
        parts = ["data"] * 1000
        joined = ''.join(parts)
        buffer = StringIO()
        for part in parts:
            buffer.write(part)
        result = buffer.getvalue()
        self.assertEqual(joined, result)

    def test_real_world_parsing(self):
        csv_line = "name,age,city\nAda,21,London\nBob,30,Paris"
        rows = [row.split(',') for row in csv_line.split('\n')]
        self.assertEqual(rows[1][0], "Ada")
        log_line = "2025-10-22 10:00:00 INFO User logged in"
        date, time, level, *msg = log_line.split()
        self.assertEqual(date, "2025-10-22")
        json_str = '{"name": "Ada", "age": 21, "city": "London"}'
        parsed = json.loads(json_str)
        self.assertEqual(parsed["name"], "Ada")

if __name__ == "__main__":
    unittest.main()
