
from collections import deque
from typing import Optional


# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


# Method: BFS
# Handle 2 cases: 
#   1) if node has left and right, then: node.left.next --> node.right
#   2) If node has next, then: node.right.next --> node.next.left
class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        queue = deque([root] if root else [])

        while queue:      
            node = queue.popleft()
            # Case 1
            if node.left and node.right:
                node.left.next = node.right
                # Case 2
                if node.next:
                    node.right.next = node.next.left
                            
                queue.append(node.left)
                queue.append(node.right)
        return root
