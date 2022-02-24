# URLify: Write a method to replace all spaces in a string with '%20'. You may assume that the string has sufficient space at the end to hold the additional characters, and that you are given the 'true' length of the string. 
# Input: "Mr John Smith      ", 13
# Output: "Mr%20John%20Smith"


def urlify(string):
    result = ""
    trimmed = string.strip()
    for i in range(len(trimmed)):
        if trimmed[i] == " ":
            result += "%20"
        else:
            result += trimmed[i]

    return result


print(urlify("Mr John Smith     "))