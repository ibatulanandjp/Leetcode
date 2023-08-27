# Method: Use 2 pointers
# TC: O(n)
# SC: O(1)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0

        for right in range(len(haystack)):
            matchLen = right - left + 1
            if haystack[left:right+1] == needle[:matchLen]:
                if matchLen == len(needle):
                    return left
            else:
                left += 1
        return -1
