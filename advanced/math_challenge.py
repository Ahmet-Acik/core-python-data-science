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