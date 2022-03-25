# Given an array of integers arr and an integer k, find the kth largest element.

# Input: arr = [4,2,9,7,5,6,7,1,3], k = 4
# Output: 6

# Notes/Brainstorm
# 1: sort then get k from end index, sort is O(n log n) with Timsort
# 2: while k greater than 0, loop and track max, then pop. when k is 0, return tracked max

# time: O(n log n)
# space: O(1)
def k_largest_elem_a(arr, k):
    arr.sort()
    return arr[-k]


# time: O(kn)
# space: O(1)
def k_largest_elem_b(arr, k):
    while k > 0:
        i = 0
        max_num = arr[0]
        while i < len(arr) - 1:
            max_num = max(arr[i], max_num)
            i += 1
        arr.remove(max_num)
        k -= 1
    return max_num


# smh .. way easier implementation than "k_largest_elem_b"
def k_largest_elem_c(arr, k):
    for i in range(k - 1):
        arr.remove(max(arr))
    return max(arr)


print(k_largest_elem_b([4, 2, 9, 7, 5, 6, 7, 1, 3], 4))
