# Method: Use Dynamic Programming (2D) with 1 extra row and col
# TC: O(n * m)
# SC: O(n * m)
from typing import List


class Solution:
    def maxDotProduct(self, nums1: List[int], nums2: List[int]) -> int:
        n, m = len(nums1), len(nums2)
        dp = [[float('-inf')] * (m + 1) for _ in range(n + 1)]

        for i in range(1, n + 1):
            for j in range(1, m + 1):
                curr_prod = nums1[i-1] * nums2[j-1]
                # Max of dp[i][j], curr_prod, left, above, and (curr_prod + aboveleft)
                dp[i][j] = max(dp[i][j], curr_prod, dp[i-1][j],
                               dp[i][j-1], curr_prod + dp[i-1][j-1])
        return dp[n][m]
