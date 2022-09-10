class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        dict = {")": "(", "]": "[", "}": "{"}

        for ch in s:
            if ch in dict.values():
                stack.append(ch)
            elif ch in dict.keys():
                if stack == [] or dict.get(ch) != stack.pop():
                    return False
            else:
                return False

        return stack == []

sol = Solution()
res = sol.isValid("()")
print(res)
