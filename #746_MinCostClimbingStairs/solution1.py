# Method: Use Dynamic Programming to store total minimum cost at each index
# Returning the minimum of last and second last element from list as result
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
