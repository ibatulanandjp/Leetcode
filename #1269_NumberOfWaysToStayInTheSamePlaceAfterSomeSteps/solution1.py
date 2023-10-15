# Method: Use Dynamic Programming (Top-Down with Memoization)
# Calculate the total number of ways for all the cases with "Stay", "Left", and "Right", memoizing for next calculation
# TC: O(n * min(n, m)), where n is steps, m is arrLen
# SC: O(n * min(n, m))
from functools import cache


class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:

        @cache  # Memoized function
        def dp(curr, remain):
            # Base Case - if no steps remaining
            if remain == 0:
                # If current index is at "0", then return 1, else 0
                if curr == 0:
                    return 1
                return 0

            # Case when "Stay"
            ans = dp(curr, remain - 1)
            # Case when "Left"
            if curr > 0:
                ans = (ans + dp(curr - 1, remain - 1)) % MOD
            # Case when "Right"
            if curr < arrLen - 1:
                ans = (ans + dp(curr + 1, remain - 1)) % MOD

            return ans

        MOD = 10**9 + 7
        return dp(0, steps)
