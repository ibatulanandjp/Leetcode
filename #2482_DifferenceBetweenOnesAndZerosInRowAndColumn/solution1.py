# Method: Calculate 1s row and 1s column, and then count
# TC: O(m * n)
# SC: O(m * n)
from typing import List


class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        m, n = len(grid), len(grid[0])
        res = [[0] * n for _ in range(m)]

        ones_row = [row.count(1) for row in grid]
        ones_col = [col.count(1) for col in zip(*grid)] # zip(*grid) transpose Matrix

        for i in range(m):
            for j in range(n):
                res[i][j] = ones_row[i] + ones_col[j] - \
                    (m - ones_row[i]) - (n - ones_col[j])

        return res
