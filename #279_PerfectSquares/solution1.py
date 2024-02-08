# Method: Use Dynamic Programming to find the min count of perfect squares using previous calculations
# TC: O(n * sqrt(n))
# SC: O(n)
class Solution:
    def numSquares(self, n: int) -> int:
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            min_count = float('inf')
            j = 1
            while j * j <= i:
                min_count = min(min_count, dp[i - j * j] + 1)
                j += 1
            dp[i] = min_count
        return dp[n]