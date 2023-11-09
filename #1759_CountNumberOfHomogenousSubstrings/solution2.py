# Method: Go on adding consecutive occurences (r - l + 1) of a character to calculate totalCount
# TC: O(n), where n is the length of the string
# SC: O(1), since only constant extra space is used.
class Solution:
    def countHomogenous(self, s: str) -> int:
        totalCount = 0
        MOD = 10 ** 9 + 7

        l = 0
        for r in range(len(s)):
            if s[l] == s[r]:
                totalCount += (r - l + 1)
            else:
                totalCount += 1
                l = r

        return totalCount % MOD