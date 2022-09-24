from collections import deque
from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        rows, cols = len(grid), len(grid[0])
        visited = set()
        islands = 0
        
        def bfs(r, c):
            queue = deque()
            visited.add((r, c))
            queue.append((r, c))
            
            # Direction coordinates
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            
            # Until queue is not empty
            while queue:
                
                # Pop 1 tuple from the set
                r, c = queue.popleft()
                
                # Check all the directions of the current coordinate
                for dr, dc in directions:
                    row = r + dr
                    col = c + dc
                    
                    # If row and col are in range, is island, and is not visited
                    if (row in range(rows) and
                        col in range(cols) and
                        grid[row][col] == "1" and
                        (row, col) not in visited):
                        # Mark visited and push into the queue 
                        visited.add((row, col))
                        queue.append((row, col))
                    
            
        for r in range(rows):
            for c in range(cols):
                # If current position is an island and is not visited already
                if grid[r][c]=="1" and (r, c) not in visited:
                    bfs(r, c)
                    islands += 1
                
        return islands