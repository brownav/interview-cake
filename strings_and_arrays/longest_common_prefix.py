class Solution:
    def longestCommonPrefix(self, strs):
        if len(strs) == 0:
            return ""

        i = 1
        j = 0
        count = len(strs[0]) - 1
        word = strs[0]
        while i < len(strs):
            while strs[i].startswith(word[0:j]):
                j += 1
            count = min(count, j - 1)
            j = 0
            i += 1

        if count == 0:
            return ""
        else:
            return word[0:count]


# Driver Code:
solution = Solution()
print(solution.longestCommonPrefix(["flower", "flow", "flight"]))
