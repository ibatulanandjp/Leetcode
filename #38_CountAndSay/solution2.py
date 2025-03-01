# Method: Iteratively convert the integer to charCountString
# TC: O(n * m), where m is the max string length
# SC: O(m), where m is the max string length
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1: return "1"
        s = "1"
        for _ in range(n-1):
            ans, i = "", 0
            while i < len(s):
                count = 1
                while i + 1 < len(s) and s[i] == s[i+1]:
                    count += 1
                    i += 1
                ans += str(count) + s[i]
                i += 1
            s = ans
        return s