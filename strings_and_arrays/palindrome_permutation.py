# Palindrome Permutation: Given a string, write a function to check if it is a permutation of a palindrome. A palindrome is a word or phrase that is the same forwards and backwards. A permutation is a rearrangement of letters. 
# Input: Tact Coa
# Output: True (permutations: "taco cat", "atco cta", etc.)

# True, it's odd: aacctto

# Brainstorm:
# for even len, you just need even num of each letter
# for odd len, every char needs even num except for one
# use dictionary to track totals

def palindrome_permutation(word):
    chars = {}
    size = 0

    for char in word:
        if char != " ":
            size += 1
            if char in chars:
                chars[char] += 1
            else:
                chars[char] = 1

    if size % 2 == 0:
        for char in chars:
            if chars[char] % 2 != 0:
                return False
    else:
        odd_allowed = 1
        for char in chars:
            if chars[char] % 2 != 0 and odd_allowed == 0:
                return False
            if chars[char] % 2 != 0:
                odd_allowed -= 1
    return True


print(palindrome_permutation("atcooooo c ta"))