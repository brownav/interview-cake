# Is Unique: Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?

# "backyard" - False
# "blockage" - True

# time: O(n)
# space: O(n)
def is_unique(word):
    chars = set()

    for char in word:
        if char in chars:
            return False
        else:
            chars.add(char)
    return True


# time: O(n log n)
# space: O(1)
def is_unique(word):
    sorted_word = sorted(word)
    for i in range(len(sorted_word)):
        if sorted_word[i] == sorted_word[i + 1]:
            return False
    return True


print(is_unique("backyzz"))
