import unittest
from advanced import math_challenge

class TestMathChallenges(unittest.TestCase):
    def test_is_prime(self):
        self.assertTrue(math_challenge.is_prime(17))
        self.assertFalse(math_challenge.is_prime(18))

    def test_sieve_primes(self):
        self.assertEqual(math_challenge.sieve_primes(10), [2, 3, 5, 7])

    def test_factorial(self):
        self.assertEqual(math_challenge.factorial(5), 120)
        self.assertEqual(math_challenge.factorial(0), 1)

    def test_fibonacci(self):
        self.assertEqual(math_challenge.fibonacci(7), 13)

    def test_fibonacci_sequence(self):
        self.assertEqual(math_challenge.fibonacci_sequence(10), [0, 1, 1, 2, 3, 5, 8])

    def test_gcd(self):
        self.assertEqual(math_challenge.gcd(48, 18), 6)

    def test_lcm(self):
        self.assertEqual(math_challenge.lcm(12, 15), 60)

    def test_count_digits(self):
        self.assertEqual(math_challenge.count_digits(12345), 5)
        self.assertEqual(math_challenge.count_digits(-9876), 4)

    def test_sum_digits(self):
        self.assertEqual(math_challenge.sum_digits(1234), 10)
        self.assertEqual(math_challenge.sum_digits(-5678), 26)

    def test_reverse_integer(self):
        self.assertEqual(math_challenge.reverse_integer(1234), 4321)
        self.assertEqual(math_challenge.reverse_integer(-5678), -8765)

    def test_is_armstrong(self):
        self.assertTrue(math_challenge.is_armstrong(153))
        self.assertFalse(math_challenge.is_armstrong(123))

    def test_factors(self):
        self.assertEqual(math_challenge.factors(28), [1, 2, 4, 7, 14, 28])
        self.assertEqual(math_challenge.factors(36), [1, 2, 3, 4, 6, 9, 12, 18, 36])

    def test_is_num_palindrome(self):
        self.assertTrue(math_challenge.is_num_palindrome(1221))
        self.assertFalse(math_challenge.is_num_palindrome(1234))

    def test_nth_root(self):
        self.assertAlmostEqual(math_challenge.nth_root(27, 3), 3.0)
        self.assertAlmostEqual(math_challenge.nth_root(16, 4), 2.0)

    def test_is_perfect_square(self):
        self.assertTrue(math_challenge.is_perfect_square(49))
        self.assertFalse(math_challenge.is_perfect_square(50))

    def test_permutations(self):
        perms = math_challenge.permutations([1,2,3])
        self.assertIn((1,2,3), perms)
        self.assertIn((2,1,3), perms)
        self.assertEqual(len(perms), 6)

    def test_sum_natural(self):
        self.assertEqual(math_challenge.sum_natural(100), 5050)

    def test_sum_squares(self):
        self.assertEqual(math_challenge.sum_squares(5), 55)

    def test_sum_cubes(self):
        self.assertEqual(math_challenge.sum_cubes(3), 36)
        self.assertEqual(math_challenge.sum_cubes(4), 100)

    def test_decimal_to_binary(self):
        self.assertEqual(math_challenge.decimal_to_binary(10), "1010")
        self.assertEqual(math_challenge.decimal_to_binary(255), "11111111")

    def test_binary_to_decimal(self):
        self.assertEqual(math_challenge.binary_to_decimal("1010"), 10)
        self.assertEqual(math_challenge.binary_to_decimal("11111111"), 255)

if __name__ == '__main__':
    unittest.main()
