# Method: Use BFS with bitmask
# TC: O(2^n * n), where n is the number of nodes. This is because there are 2^n possible subsets of nodes and n nodes to consider for each subset.
# SC: O(2^n * n), needed for the visited set and the queue.
from typing import List
from collections import deque


class Solution:
    def shortestPathLength(self, graph: List[List[int]]) -> int:
        n = len(graph)
        queue = deque([(1 << i, i, 0) for i in range(n)]) # A queue with (mask, node, dist)
        visited = set((1 << i, i) for i in range(n)) # Visited nodes set with (mask, node)

        while queue:
            mask, node, distance = queue.popleft()

            # If all the nodes have been visited
            if mask == (1 << n) - 1:
                return distance
            
            # For all the neighbors of current node
            for neighbor in graph[node]:
                # Calculate new mask for neighbor, and if it's not visited, add it to the queue and visited list
                new_mask = mask | (1 << neighbor)
                if (new_mask, neighbor) not in visited:
                    visited.add((new_mask, neighbor))
                    queue.append((new_mask, neighbor, distance + 1))
