from collections import deque
from typing import List, Optional

# Definition for a Node.


class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':

        level_order = self.levelOrder(root)

        for level in level_order:
            for i in range(len(level)):
                if i < len(level)-1:
                    level[i].next = level[i+1]

        return root

    def levelOrder(self, root: 'Optional[Node]') -> 'List[List[Node]]':

        if not root:
            return []
        queue = deque([root])
        level_order = []

        while queue:
            level = []
            for _ in range(len(queue)):
                node = queue.popleft()
                level.append(node)

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            if level:
                level_order.append(level)

        return level_order
