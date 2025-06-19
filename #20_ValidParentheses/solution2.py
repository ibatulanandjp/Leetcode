# Method: Stack implementation
# TC: O(n)
# SC: O(n)
class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        p_dict = {')': '(', '}': '{', ']': '['}

        for ch in s:
            if ch in p_dict:
                if stack and stack[-1] == p_dict[ch]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(ch)
        return True if not stack else False
