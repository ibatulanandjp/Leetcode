# Method: Use DFS to traverse the graph and mark nodes as "0" in the grid to avoid revisiting
# Increment the number of islands when conditions satisfy
# TC: O(n * m), where n is the number of rows and m is the number of columns
# SC: O(n * m)
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0

        def dfs(r, c):
            if (r not in range(ROWS) or
                c not in range(COLS) or
                grid[r][c] != "1"
            ):
                return

            grid[r][c] = "0"
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    dfs(r, c)
                    islands += 1

        return islands