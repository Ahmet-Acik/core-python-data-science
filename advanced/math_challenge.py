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