# Method: Use Dynamic Programming (Bottom-up)
# Calculate the total number of ways for all the cases with "Stay", "Left", and "Right"
# TC: O(n * min(n, m)), where n is steps, m is arrLen; nested for-loops iterate over O(n * min(n,m)) states of (curr, remain). Calculating each state is done in O(1)
# SC: O(n * min(n, m))
class Solution:
    def numWays(self, steps: int, arrLen: int) -> int:
        MOD = 10 ** 9 + 7
        arrLen = min(arrLen, steps)

        # To store -> dp[curr][remain]
        dp = [[0] * (steps + 1) for _ in range(arrLen)]
        dp[0][0] = 1

        for remain in range(1, steps + 1):
            for curr in range(arrLen - 1, -1, -1):
                # Case when "Stay"
                ans = dp[curr][remain - 1]
                # Case when "Left"
                if curr > 0:
                    ans = (ans + dp[curr - 1][remain - 1]) % MOD
                # Case when "Right"
                if curr < arrLen - 1:
                    ans = (ans + dp[curr + 1][remain - 1]) % MOD

                dp[curr][remain] = ans
        return dp[0][steps]
