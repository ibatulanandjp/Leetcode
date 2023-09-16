# Method: Use Djikstra's Algorithm with Priority Queue (Heap)
# TC: O(m*n*log⁡(m*n))
# SC: O(m*n)
from typing import List
import math
from heapq import heappop, heappush


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        ROWS, COLS = len(heights), len(heights[0])
        directions = [[-1, 0], [1, 0], [0, -1], [0, 1]]

        # Initialize the distance matrix
        distance = [[math.inf for _ in range(COLS)] for _ in range(ROWS)]
        distance[0][0] = 0
        min_heap = [(0, 0, 0)]  # Priority Queue with [(effort, row, col)]

        while min_heap:
            effort, row, col = heappop(min_heap)

            # If reached the bottom-right cell, return effort
            if row == ROWS-1 and col == COLS-1:
                return effort

            # Traverse in all directions
            for dr, dc in directions:
                r, c = row + dr, col + dc
                if r in range(ROWS) and c in range(COLS):
                    new_effort = max(effort, abs(
                        heights[row][col] - heights[r][c]))

                    # If the new effort is less than current distance
                    if new_effort < distance[r][c]:
                        distance[r][c] = new_effort
                        heappush(min_heap, (new_effort, r, c))
