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



# 4. Find the missing number in 0..n
def find_missing_number(nums):
    n = len(nums)
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)
    return expected_sum - actual_sum
print("Missing number:", find_missing_number([3,0,1]))  # Output: 2


# 5. Find all pairs that sum to a target
def two_sum_pairs(nums, target):
    seen = set()
    pairs = set()
    for num in nums:
        complement = target - num
        if complement in seen:
            pairs.add(tuple(sorted((num, complement))))
        seen.add(num)
    return list(pairs)
print("Pairs summing to 6:", two_sum_pairs([3, 1, 5, 2, 4], 6))  # Output: [(2,4), (1,5), (3,3)]



# 6. Find the majority element (appears more than n/2 times)
def majority_element(nums):
    count = 0
    candidate = None
    for num in nums:
        if count == 0:
            candidate = num
            count = 1
        elif candidate == num:
            count += 1
        else:
            count -= 1
    return candidate
print("Majority element:", majority_element([2,2,1,1,1,2,2]))  # Output: 2


# 7. Rotate array right by k steps
def rotate_array(nums, k):
    k = k % len(nums)
    nums[:] = nums[-k:] + nums[:-k]
    return nums
nums3 = [1,2,3,4,5,6,7]
print("Rotate right by 3:", rotate_array(nums3, 3))  # Output: [5,6,7,1,2,3,4]


# 8. Find intersection of two arrays (unique elements)
def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
print("Intersection:", intersection([1,2,2,1], [2,2]))  # Output: [2]


# 9. Find the longest consecutive sequence
def longest_consecutive(nums):
    num_set = set(nums)
    longest = 0
    for num in num_set:
        if num - 1 not in num_set:
            length = 1
            while num + length in num_set:
                length += 1
            longest = max(longest, length)
    return longest
print("Longest consecutive:", longest_consecutive([100,4,200,1,3,2]))  # Output: 4



# 10. Product of array except self
def product_except_self(nums):
    n = len(nums)
    left, right, result = 1, 1, [1]*n
    for i in range(n):
        result[i] *= left
        left *= nums[i]
    for i in range(n-1, -1, -1):
        result[i] *= right
        right *= nums[i]
    return result
print("Product except self:", product_except_self([1,2,3,4]))  # Output: [24,12,8,6]


# 11. Find the first duplicate element
def first_duplicate(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return num
        seen.add(num)
    return None
print("First duplicate:", first_duplicate([2, 1, 3, 5, 3, 2]))  # Output: 3


# 12. Find the single number (every other appears twice)
def single_number(nums):
    result = 0
    for num in nums:
        result ^= num
    return result
print("Single number:", single_number([4,1,2,1,2]))  # Output: 4


# 13. Find all unique triplets that sum to zero
def three_sum(nums):
    nums.sort()
    res = []
    n = len(nums)
    for i in range(n):
        if i > 0 and nums[i] == nums[i-1]:
            continue
        l, r = i+1, n-1
        while l < r:
            s = nums[i] + nums[l] + nums[r]
            if s == 0:
                res.append([nums[i], nums[l], nums[r]])
                while l < r and nums[l] == nums[l+1]: l += 1
                while l < r and nums[r] == nums[r-1]: r -= 1
                l += 1; r -= 1
            elif s < 0:
                l += 1
            else:
                r -= 1
    return res
print("Three sum:", three_sum([-1,0,1,2,-1,-4]))  # Output: [[-1, -1, 2], [-1, 0, 1]]
