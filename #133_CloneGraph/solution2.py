# Method: Use BFS to clone the graph
# Time Complexity: O(V + E), where V is the number of vertices and E is the number of edges.
# Space Complexity: O(V), for the hashmap storing the cloned nodes.
from collections import deque

# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None 
            
        copyNode = {}
        copyNode[node] = Node(node.val)
        q = deque([node])

        while q:
            curr = q.popleft()
            for neighbor in curr.neighbors:
                if neighbor not in copyNode:
                    copyNode[neighbor] = Node(neighbor.val)
                    q.append(neighbor)
                copyNode[curr].neighbors.append(copyNode[neighbor])
        return copyNode[node]
