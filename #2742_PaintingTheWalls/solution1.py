# Method: Use Dynamic Programming (Memoization), to hire or not hire the paid painter, minimizing the cost
# TC: O(n^2)
# SC: O(n^2)
from functools import cache
from typing import List
from math import inf


class Solution:
    def paintWalls(self, cost: List[int], time: List[int]) -> int:
        
        @cache  # Memoized function
        def dp(i, remain):
            # Base case: Already painted all walls
            if remain <= 0:
                return 0
            # Base case: Ran out of walls to put paid painter (Impossible to assign)
            if i == n:
                return inf

            # Cost, when we hire a paid painter
            paint_cost = cost[i] + dp(i+1, remain - (1+time[i]))
            # Cost, when we don't hire a paid painter
            dont_paint_cost = dp(i+1, remain)
            return min(paint_cost, dont_paint_cost)

        n = len(cost)
        return dp(0, n)
