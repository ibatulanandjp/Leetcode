# Method: Use DFS to check for cycles and connectivity, starting from node 0.
# Add extra prev_node parameter to avoid counting the edge back to the parent as a cycle.
# TC: O(V + E), where V is the number of vertices and E is the number of edges
# SC: O(V + E) for the adjacency list and O(V) for the visited
from typing import List

class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) > (n - 1):
            return False

        adj = {i: [] for i in range(n)}
        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)
        
        visited = set()

        # graph == tree, if connected + no cycle
        def dfs(node, prev_node):
            if node in visited:
                return False

            visited.add(node)
            for neighbor in adj[node]:
                if neighbor == prev_node:
                    continue
                if not dfs(neighbor, node):
                    return False
            return True

        return dfs(0, -1) and len(visited) == n