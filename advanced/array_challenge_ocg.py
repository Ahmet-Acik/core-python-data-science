"""
array_challenge_comprehensive.py
--------------------------------
Multiple array challenge solutions demonstrating different approaches,
variable names, and edge case handling.
"""

import ast

# 1. Basic: Second lowest and second greatest (unique)
def second_lowest_greatest(nums):
    unique_sorted = sorted(set(nums))
    if len(unique_sorted) == 1:
        return f"{unique_sorted[0]} {unique_sorted[0]}"
    elif len(unique_sorted) == 2:
        return f"{unique_sorted[1]} {unique_sorted[0]}"
    else:
        return f"{unique_sorted[1]} {unique_sorted[-2]}"
print("Basic:", second_lowest_greatest([1, 2, 3, 4, 5]))  # Output: "2 4"
