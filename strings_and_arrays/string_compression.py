# String Compression: Implement a method to perform basic string compression using counts of repeated characters. If the compressed string would not become smaller than original string your method should return the original string. You can assume the string has only uppercase and lowercase letters (a-z).
# Input: aabcccccaaa
# Output: a2b1c5a3


def string_compression(string):
    result = ""
    count = 1
    current = string[0]
    for i in range(1, len(string)):
        if string[i] == current:
            count += 1
        else:
            result += current
            result += str(count)
            current = string[i]
            count = 1
    result += current
    result += str(count)

    return result if len(result) < len(string) else string


print(string_compression("aabcccccaaa"))
