# Method: Use DFS to count connected components
# TC: O (V + E), where V is the number of vertices and E is the number of edges
# SC: O (V + E) for the adjacency list and O (V) for the visited set
from typing import List

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        def dfs(node):
            if node in visited:
                return
            
            visited.add(node)
            for neighbor in adj[node]:
                dfs(neighbor)

        count = 0
        for node in range(n):
            if node not in visited:
                dfs(node)
                count += 1
        return count