# Method: For each starting character in haystack, check if the needle exists
# TC: O(n)
# SC: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack) - len(needle) + 1):
            if haystack[i:i+len(needle)] == needle:
                return i
        return -1
