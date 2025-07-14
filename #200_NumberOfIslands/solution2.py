# Method: Use BFS to traverse the graph and mark nodes as "0" in the grid to avoid revisiting
# Increment the number of islands when conditions satisfy
# TC: O(n * m), where n is the number of rows and m is the number of columns
# SC: O(n * m)
from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROWS, COLS = len(grid), len(grid[0])
        directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        islands = 0

        def bfs(r, c):
            queue = deque()
            grid[r][c] = "0"
            queue.append((r, c))

            while queue:
                r, c = queue.popleft()

                for dr, dc in directions:
                    nr, nc = r + dr, c + dc
                    if (nr not in range(ROWS) or
                        nc not in range(COLS) or
                        grid[nr][nc] == "0"
                    ):
                        continue
                    queue.append((nr, nc))
                    grid[nr][nc] = "0"
            

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "1":
                    bfs(r, c)
                    islands += 1

        return islands