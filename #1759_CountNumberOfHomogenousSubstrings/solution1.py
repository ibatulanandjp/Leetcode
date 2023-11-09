# Method: Use formula sum = n*(n+1)//2 to calculate the total count of consecutive occurences of a character.
# TC: O(n), where n is the length of the string
# SC: O(1), since only constant extra space is used.
class Solution:
    def countHomogenous(self, s: str) -> int:
        totalCount = 0
        MOD = 10 ** 9 + 7

        l = 0
        for r in range(len(s) + 1):
            if r == len(s) or s[l] != s[r]:
                n = r - l
                count = (n * (n + 1)) // 2
                totalCount += count
                l = r

        return totalCount % MOD