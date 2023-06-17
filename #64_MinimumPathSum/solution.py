# Method: Traverse from bottom-right to top-left adding the min(grid[r+1][c], grid[r][c+1]) to the current location in grid
# TC: O(m*n), since we traverse the whole grid once
# SC: O(1), since values are updated in-place
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])

        for r in range(ROWS-1, -1, -1):
            for c in range(COLS-1, -1, -1):

                if r == ROWS-1 and c == COLS-1:
                    continue
                elif r == ROWS-1:
                    grid[r][c] += grid[r][c+1]
                elif c == COLS-1:
                    grid[r][c] += grid[r+1][c]
                else:
                    grid[r][c] += min(grid[r+1][c], grid[r][c+1])

        return grid[0][0]
