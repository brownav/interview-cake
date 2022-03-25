# Given a string and a positive number k, find the longest substring of the string containing k distinct characters. If k is more than the total number of distinct characters in the string, return the whole string.

# input string: abcbdbdbbdcdabd
# input k: 2
# output: bdbdbbd

# notes: sliding window technique


def subarray_k_distinct(string, k):
    if k > len(string):
        return string

    i, j = 0, 0
    distinct = set()
    longest = ""

    while j < len(string):
        distinct.add(string[i])
        distinct.add(string[j])
        if len(distinct) > k:
            i = j - 1
            distinct.clear()
        else:
            longest = (
                longest if len(longest) > len(string[i : j + 1]) else string[i : j + 1]
            )
            j += 1

    return longest


print(subarray_k_distinct("abcbdbdbbdcdabd", 2))
print(subarray_k_distinct("abcbdbdbbdcdabd", 3))
print(subarray_k_distinct("abcbdbdbbdcdabd", 5))
