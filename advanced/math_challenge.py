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
