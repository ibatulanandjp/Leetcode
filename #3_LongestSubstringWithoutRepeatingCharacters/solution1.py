class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        seenMap = {}
        maxLength = 0
        l = 0

        for r in range(len(s)):
            if s[r] in seenMap:
                l = max(l, seenMap[s[r]]+1)
            maxLength = max(maxLength, r-l+1)
            seenMap[s[r]] = r

        return maxLength
