# Method: Use Stack to build string after removing characters with backspace
# TC: O(n)
# SC: O(n)
class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def buildString(string: str):
            stack = []
            for ch in string:
                if ch != "#":
                    stack.append(ch)
                elif stack:
                    stack.pop()
            return stack
        return buildString(s) == buildString(t)
