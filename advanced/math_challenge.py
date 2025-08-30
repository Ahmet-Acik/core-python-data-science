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
