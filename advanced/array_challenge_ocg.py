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


# 2. Remove duplicates in-place and return new length
def remove_duplicates(nums):
    if not nums:
        return 0
    write_idx = 1
    for read_idx in range(1, len(nums)):
        if nums[read_idx] != nums[write_idx-1]:
            nums[write_idx] = nums[read_idx]
            write_idx += 1
    return write_idx
nums1 = [1,1,2,2,3]
length = remove_duplicates(nums1)
print("Remove duplicates:", nums1[:length], "Length:", length)  # Output: [1,2,3] Length: 3


# 3. Move all zeros to the end (in-place)
def move_zeros(nums):
    insert_pos = 0
    for num in nums:
        if num != 0:
            nums[insert_pos] = num
            insert_pos += 1
    for i in range(insert_pos, len(nums)):
        nums[i] = 0
    return nums
nums2 = [0,1,0,3,12]
print("Move zeros:", move_zeros(nums2))  # Output: [1,3,12,0,0]
