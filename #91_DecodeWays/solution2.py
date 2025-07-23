# Method: DP (Bottom-Up through decision-tree) with space optimization
# TC: O(n), where n is the length of the string
# SC: O(1), using only constant space for dp variables
class Solution:
    def numDecodings(self, s: str) -> int:
        dp = dp2 = 0
        dp1 = 1
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp = 0
            else:
                dp = dp1
            
            if i + 1 < len(s) and (s[i] == "1" or 
                (s[i] == "2" and s[i + 1] in "0123456")
            ):
                dp += dp2
            dp, dp1, dp2 = 0, dp, dp1
            
        return dp1