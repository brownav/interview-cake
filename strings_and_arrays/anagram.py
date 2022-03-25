# Given two strings s1 and s2, check if they're anagrams. Two strings are anagrams if they're made of the same characters with the same frequencies, just in a different order.

# Input: s1 = "danger", s2 = "garden"
# Output: True

# Notes/Brainstorm:
# 1. traverse one string,for each char check if char is in second string (this seems slow/bad and won't account for char frequency)
# 2. exit early if len is not same, they can't be anagrams
# 3. sort both, then traverse at same time and check for char equality. casing matters for built-in sort.
# 4. use extra storage to keep track of char appearance, traverse both strings and store, then analyze storage/map to determine

# time: O(n log n) -> sorted() uses Timsort
# space: O(1)
def is_anagram_a(str1, str2):
    if len(str1) != len(str2):
        return False

    return sorted(str1.lower()) == sorted(str2.lower())


# time: O(n)
# space: O(n)
def is_anagram_b(str1, str2):
    if len(str1) != len(str2):
        return False

    str1_chars = {}
    str2_chars = {}
    for char in str1:
        if char in str1_chars:
            str1_chars[char] += 1
        else:
            str1_chars[char] = 1
    for char in str2:
        if char in str2_chars:
            str2_chars[char] += 1
        else:
            str2_chars[char] = 1

    for key in str1_chars:
        if key not in str2_chars or str1_chars[key] != str2_chars[key]:
            return False

    return True


def checkPermutation(s1, s2):
    if len(s1) != len(s2):
        return False

    count = {}
    for i in s1:
        count[i] = count.get(i, 1) + 1
    for i in s2:
        if i in count:
            count[i] -= 1
            if count[i] == 0:
                del count[i]
        else:
            return False
    return len(count) == 0


print(checkPermutation("tacocat", "tacocat"))
