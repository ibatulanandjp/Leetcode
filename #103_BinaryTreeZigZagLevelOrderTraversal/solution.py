from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Method: Implement BFS using Queue (Level order traversal) 
# And change the direction at alternate level (Reverse)
# TC: O(n)
# SC: O(n)
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Initialize queue with [root] if it exists
        queue = deque([root] if root else [])
        zigzag_level_order = []
        direction = 1

        while queue:
            # List of each level elements
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                
                if node:
                    level.append(node.val)
                    queue.append(node.left)
                    queue.append(node.right)

            # Reverse the level list alternately
            if level:
                zigzag_level_order.append(level[::direction])
                direction *= (-1)

        return zigzag_level_order
