import unittest
from advanced import string_challenge1

class TestStringChallenges(unittest.TestCase):
    def test_reverse_string(self):
        self.assertEqual(string_challenge1.reverse_string('hello'), 'olleh')
        self.assertEqual(string_challenge1.reverse_string(''), '')

    def test_is_palindrome(self):
        self.assertTrue(string_challenge1.is_palindrome('madam'))
        self.assertFalse(string_challenge1.is_palindrome('hello'))

    def test_are_anagrams(self):
        self.assertTrue(string_challenge1.are_anagrams('listen', 'silent'))
        self.assertFalse(string_challenge1.are_anagrams('hello', 'world'))

    def test_first_unique_char(self):
        self.assertEqual(string_challenge1.first_unique_char('leetcode'), 0)
        self.assertEqual(string_challenge1.first_unique_char('aabb'), -1)

    def test_length_of_longest_substring(self):
        self.assertEqual(string_challenge1.length_of_longest_substring('abcabcbb'), 3)
        self.assertEqual(string_challenge1.length_of_longest_substring('bbbbb'), 1)

    def test_compress_string(self):
        self.assertEqual(string_challenge1.compress_string('aabcccccaaa'), 'a2b1c5a3')
        self.assertEqual(string_challenge1.compress_string('abc'), 'a1b1c1')

    def test_string_permutations(self):
        perms = string_challenge1.string_permutations('abc')
        self.assertIn('abc', perms)
        self.assertIn('bca', perms)
        self.assertEqual(len(perms), 6)

    def test_count_vowels_consonants(self):
        v, c = string_challenge1.count_vowels_consonants('hello')
        self.assertEqual(v, 2)
        self.assertEqual(c, 3)

if __name__ == '__main__':
    unittest.main()
