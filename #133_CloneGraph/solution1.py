# Method: Use DFS to clone the graph
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V), for the hashmap storing the cloned nodes.

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        nodeCopy = {}

        def dfs(node):
            if node in nodeCopy:
                return nodeCopy[node]
            
            copy = Node(node.val)
            nodeCopy[node] = copy
            for neighbor in node.neighbors:
                copy.neighbors.append(dfs(neighbor))
            return copy

        return dfs(node) if node else None