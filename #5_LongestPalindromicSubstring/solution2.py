# Method: Dynamic Programming - dp matrix with upper diagonal (move bottom-up left-right)
# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = s[0]
        # Initialize dp matrix with "0"
        dp = [[0] * len(s) for _ in range(len(s))]

        # Fill diagonal cells with "1"
        for i in range(len(s)):
            dp[i][i] = 1

        # Go from bottom-up and left-right
        for i in range(len(s)-1, -1, -1):
            for j in range(i+1, len(s)):
                # If values at i and j are same, and (either a single char, or inner string is a palindrome)
                if s[i] == s[j] and (j == i+1 or dp[i+1][j-1] == 1):
                    dp[i][j] = 1

                    # Update res
                    if len(res) < len(s[i:j+1]):
                        res = s[i:j+1]

        return res
