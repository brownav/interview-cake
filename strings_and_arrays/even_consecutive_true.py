### Problem ###
# You are given an array that can only contain 1s and 0s. Method should return true if ALL consecutive sequences of 1s are even in length, otherwise return false.
# 010 --> false; 0101 --> false; 011011 -> true; 0110111 -> false; 00 --> true


### Notes ###
# objective: if all consecutive sequences of 1 are even, return true; else false
# track consecutive sequences of 1s, determine if they are even
# when come across a 1, keep count until we hit 0; if count is odd then return false


def even_consecutive_true(nums):
    consecutive_ones = 0

    for i in range(len(nums)):
        if nums[i] == 1:
            consecutive_ones += 1

        # if last elem is not a 0 we still need to verify even consecutive count before exiting
        if nums[i] == 0 or i == len(nums) - 1:
            if consecutive_ones % 2 != 0:
                return False
            consecutive_ones = 0

    return True


print(even_consecutive_true([0, 1, 0]))
print(even_consecutive_true([0, 1, 0, 1]))
print(even_consecutive_true([0, 1, 1, 0, 1, 1, 1]))
print(even_consecutive_true([0, 1, 1, 0, 1, 1]))
print(even_consecutive_true([0, 0]))
