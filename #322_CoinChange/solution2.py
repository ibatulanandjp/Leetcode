# Method: Dynamic Programming (Top-Down Approach) using memoization
# Use recursion to explore all combinations of coins, storing results in a memoization dictionary
# TC: O(n * t), where n is the number of coins and t is the target amount
# SC: O(t), where t is the target amount (due to recursion stack depth)
from typing import List

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}

        def dfs(amount):
            if amount == 0:
                return 0
            if amount in memo:
                return memo[amount]
            
            res = 1e9
            for coin in coins:
                if amount - coin >= 0:
                    res = min(res, 1 + dfs(amount - coin))
            
            memo[amount] = res
            return res
        
        min_coins = dfs(amount)
        return -1 if min_coins >= 1e9 else min_coins