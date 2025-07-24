# Method: Dynamic Programming (Bottom-Up Approach) tracking a list of coins required for every value (0 ... amount)
# Use the previously stored values to compute the minimum required no. of coins
# TC: O(n * t), where n is the number of coins and t is the target amount
# SC: O(t), where t is the target amount
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:

        # Create a list with values [0, inf, inf, inf, ...] for (0 ... amount)
        dp = [0] + [float('inf') for i in range(1, amount + 1)]

        # For each value in (1 ... amount)
        for a in range(1, amount+1):
            # For each available coin
            for c in coins:
                # If adding current coin doesn't exceed the current amount
                if a - c >= 0:
                    # New dp[a] should be min of current dp[a] and (1 + dp[a-c]); "1" because 1 coin is added
                    dp[a] = min(dp[a], 1 + dp[a - c])

        # Return if dp[amount] isn't the original one, else -1
        return dp[amount] if dp[amount] != float('inf') else -1
