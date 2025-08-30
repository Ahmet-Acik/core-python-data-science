"""
math_challenge.py
-----------------
Comprehensive math and number-based coding challenges for interviews and practice.
Each challenge demonstrates a different mathematical or algorithmic concept.
"""

# 1. Check if a number is prime
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True
print("Is 17 prime?", is_prime(17))  # Output: True
print("Is 18 prime?", is_prime(18))  # Output: False


# 2. Find all primes up to n (Sieve of Eratosthenes)
def sieve_primes(n):
    sieve = [True] * (n+1)
    sieve[0:2] = [False, False]
    for i in range(2, int(n**0.5)+1):
        if sieve[i]:
            for j in range(i*i, n+1, i):
                sieve[j] = False
    return [i for i, is_p in enumerate(sieve) if is_p]
print("Primes up to 30:", sieve_primes(30))  # Output: [2, 3, 5, 7, 11, 13, 17, 19, 23, 29]


# 3. Compute factorial
def factorial(n):
    result = 1
    for i in range(2, n+1):
        result *= i
    return result
print("Factorial 5:", factorial(5))  # Output: 120
print("Factorial 0:", factorial(0))  # Output: 1


# 4. Compute nth Fibonacci number (iterative)
def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a
print("Fibonacci(7):", fibonacci(7))  # Output: 13

# All Fibonacci numbers up to n
def fibonacci_sequence(n):
    seq = []
    a, b = 0, 1
    while a <= n:
        seq.append(a)
        a, b = b, a + b
    return seq
print("Fibonacci sequence up to 50:", fibonacci_sequence(50))  # Output: [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]


# 5. Greatest common divisor (GCD)
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a
print("GCD of 48 and 18:", gcd(48, 18))  # Output: 6


# 6. Least common multiple (LCM)
def lcm(a, b):
    return abs(a * b) // gcd(a, b)
print("LCM of 12 and 15:", lcm(12, 15))  # Output: 60


# 7. Count number of digits
def count_digits(n):
    return len(str(abs(n)))
print("Digits in 12345:", count_digits(12345))  # Output: 5
print("Digits in -9876:", count_digits(-9876))  # Output: 4


# 8. Sum of digits
def sum_digits(n):
    return sum(int(d) for d in str(abs(n)))
print("Sum of digits in 1234:", sum_digits(1234))  # Output: 10
print("Sum of digits in -5678:", sum_digits(-5678))  # Output: 26


# 9. Reverse an integer
def reverse_integer(n):
    sign = -1 if n < 0 else 1
    reversed_num = int(str(abs(n))[::-1])
    return sign * reversed_num
print("Reverse 1234:", reverse_integer(1234))  # Output: 4321
print("Reverse -5678:", reverse_integer(-5678))  # Output: -8765


# 10. Check if a number is an Armstrong number, also known as a narcissistic number
def is_armstrong(n):
    digits = str(n)
    power = len(digits)
    return n == sum(int(d)**power for d in digits)
print("Is 153 Armstrong?", is_armstrong(153))  # Output: True
print("Is 123 Armstrong?", is_armstrong(123))  # Output: False


# 11. Find all factors of a number
def factors(n):
    result = set()
    for i in range(1, int(n**0.5)+1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)
    return sorted(result)
print("Factors of 28:", factors(28))  # Output: [1, 2, 4, 7, 14, 28]
print("Factors of 36:", factors(36))  # Output: [1, 2, 3, 4, 6, 9, 12, 18, 36]


# 12. Check if a number is a palindrome
def is_num_palindrome(n):
    s = str(n)
    return s == s[::-1]
print("Is 1221 palindrome?", is_num_palindrome(1221))  # Output: True
print("Is 1234 palindrome?", is_num_palindrome(1234))  # Output: False


# 13. Find the nth root of a number
def nth_root(x, n):
    return x ** (1/n)
print("Cube root of 27:", nth_root(27, 3))  # Output: 3.0
print("Fourth root of 16:", nth_root(16, 4))  # Output: 2.0


# 14. Check if a number is a perfect square
def is_perfect_square(n):
    root = int(n ** 0.5)
    return root * root == n
print("Is 49 a perfect square?", is_perfect_square(49))  # Output: True
print("Is 50 a perfect square?", is_perfect_square(50))  # Output: False


# 15. Generate all permutations of a list of numbers
def permutations(nums):
    from itertools import permutations
    return list(permutations(nums))
print("Permutations of [1,2,3]:", permutations([1,2,3]))  # Output: [(1,2,3), (1,3,2), ...]


# 17. Find the sum of the first n squares
def sum_squares(n):
    return n * (n + 1) * (2 * n + 1) // 6
print("Sum of first 5 squares:", sum_squares(5))  # Output: 55
