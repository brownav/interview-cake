# Given string, print how often each char appears and remove duplicate chars. Return string without duplicate chars.
# jamesrussellbennett -> jamrubt

# Notes
# keep track of how many dupes are being removed
# count appearance of words

# create dict/hashmap where key is word, value is count
# iterate over string and keep count, return new string where value equals 1

def remove_dupes(string):
    word_count = {}

    for char in string: 
        if char in word_count:
            word_count[char] += 1
        else:
            word_count[char] = 1

    no_dupes = ""

    for char in word_count:
        print(f'char {char} appears {word_count[char]} times')
        if word_count[char] == 1:
            no_dupes += char

    return no_dupes

print(remove_dupes("jamesrussellbennet"))
print(remove_dupes("alexandriavictoriabrown"))