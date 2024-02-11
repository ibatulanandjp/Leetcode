# Method: Use dynamic programming with memoization and calculate maximum cherries to collect
# TC: O(r * c^2)
# SC: O(r * c^2)
from typing import List


class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        rows, cols = len(grid), len(grid[0])
        memo = {}

        def dp(r: int, c1: int, c2: int):
            # Base case
            if r == rows or c1 not in range(cols) or c2 not in range(cols):
                return 0

            # Check in memoization dictionary
            if (r, c1, c2) in memo:
                return memo[(r, c1, c2)]

            # Collect current cherries
            cherries = grid[r][c1] + (grid[r][c2] if c1 != c2 else 0)

            # Calculate maximum cherries collected by both robots in the next row
            max_cherries = 0
            for dc1 in [-1, 0, 1]:
                for dc2 in [-1, 0, 1]:
                    max_cherries = max(max_cherries, dp(
                        r + 1, c1 + dc1, c2 + dc2))

            # Add the cherries and memoize
            result = cherries + max_cherries
            memo[(r, c1, c2)] = result
            return result

        # Start from top row
        return dp(0, 0, cols - 1)
