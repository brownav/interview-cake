class Solution:
    def isValid(self, s: str) -> bool:
        if (len(s) % 2) != 0:
            return False

        left_parens = []
        for char in s:
            if char in ["{", "(", "["]:
                left_parens.append(char)
            elif left_parens and char == "}" and left_parens[-1] == "{":
                left_parens.pop()
            elif left_parens and char == ")" and left_parens[-1] == "(":
                left_parens.pop()
            elif left_parens and char == "]" and left_parens[-1] == "[":
                left_parens.pop()
            else:
                return False

        return len(left_parens) == 0


solution = Solution()
print(solution.isValid("([])"))
