# Method: Dynamic Programming - Store all the possible combination of sum from 0 to target
# TC: O(n*target)
# SC: O(target)
from typing import List


class Solution:
    def combinationSum4(self, nums: List[int], target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1

        # For numbers from 1 to target, calculate dp (combinations)
        for i in range(1, target + 1):
            # For each number in the list
            for n in nums:
                # If i is greater than n, add the (i-n)th value to (i)th value in dp
                if i-n >= 0:
                    dp[i] += dp[i-n]

        return dp[target]
