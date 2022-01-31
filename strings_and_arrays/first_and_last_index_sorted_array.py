# Given a sorted array of integers arr and an integer target, find the index of the first and last position of target in arr. If target can't be found in arr, return [-1,-1]

# Input: arr = [2,4,5,5,5,5,5,7,9,9], target = 5
# Output: [2,6]

# time: O(n)
# space: O(1)
def first_and_last_a(arr, target):
    first_index = None
    last_index = None
    loop = 0

    for i in range(len(arr)):
        if arr[i] == target:
            first_index = i
            loop = i
            break

    while loop < len(arr):
        if arr[loop] == target:
            last_index = loop
            loop += 1
        else:
            break

    if first_index is not None and last_index is not None:
        return [first_index, last_index]
    else:
        return [-1, -1]

# ------------------------------------------ #

# time = O(log n)
# space = O(1)
def first_and_last_b(arr, target):
    if len(arr) == 0 or arr[0] > target or arr[-1] < target:
        return [-1, -1]

    first = find_first(arr, target)
    last = find_last(arr[first:], target)

    return [first, first+last]


def find_first(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target and arr[mid-1] < target:
            return mid
        elif arr[mid] < target:
            start = mid + 1
        else: 
            end = mid - 1

    return -1

def find_last(arr, target):
    start = 0
    end = len(arr)-1

    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target and arr[mid+1] > target:
            return mid
        elif arr[mid] > target:
            end = mid - 1
        else:
            start = mid + 1

    return -1


print(first_and_last_b([2,4,5,5,5,5,5,5,9,9], 5))



