# Method: Use XOR to find the extra character
# TC: O(n), where n is the length of the string
# SC: O(1)

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        res = 0
        for ch in s + t:
            res ^= ord(ch)
        return chr(res)
