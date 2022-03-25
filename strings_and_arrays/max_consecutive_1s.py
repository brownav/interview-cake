from typing import List

# Given a binary array, find the maximum number of consecutive 1s in this array.

# Input: [1,1,0,1,1,1]
# Output: 3

# Note:
# The input array will only contain 0 and 1.
# The length of input array is a positive integer and will not exceed 10,000


def max_consecutive_ones(nums: List) -> List:
    if not nums:
        return 0

    max_so_far, current_max = 0, 0
    for i in range(len(nums)):
        if nums[i] == 1:
            current_max += 1
        else:
            max_so_far = max(max_so_far, current_max)
            current_max = 0

    if nums[-1] == 0:
        max_so_far = max(max_so_far, current_max)

    return max_so_far


print(max_consecutive_ones([1, 1, 0, 1, 1, 1, 1, 1, 1, 0, 1]))
print(max_consecutive_ones([]))
