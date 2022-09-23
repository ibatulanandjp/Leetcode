from typing import List, Optional

# Definition for a binary tree node.


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:

        if not root:
            return []

        queue = deque([root])
        zigzag_level_order = []
        direction = 1

        while queue:
            level = []
            for i in range(len(queue)):
                node = queue.popleft()
                level.append(node.val)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            zigzag_level_order.append(level[::direction])
            direction *= (-1)

        return zigzag_level_order
