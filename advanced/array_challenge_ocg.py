"""
array_challenge_interview_set.py
--------------------------------
A collection of classic array/list challenges for interviews.
Each challenge uses clear, unique variable names and demonstrates a different concept.
"""

# 1. Find the maximum sum subarray (Kadane's Algorithm)
def max_subarray_sum(arr):
    max_sum = current_sum = arr[0]
    for num in arr[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    return max_sum
print("Max subarray sum:", max_subarray_sum([-2,1,-3,4,-1,2,1,-5,4]))  # Output: 6

