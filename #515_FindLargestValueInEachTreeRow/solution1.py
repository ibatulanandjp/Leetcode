# Method: Use BFS, keeping the maximum from each level into a result array
# TC: O(n), where n is the no. of nodes in the tree
# SC: O(n)

from typing import List, Optional
from collections import deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        res = []
        queue = deque([[root]])
        while queue:
            curr_level = queue.popleft()
            curr_max = float('-inf')
            next_level = []
            for node in curr_level:
                curr_max = max(curr_max, node.val)
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            if next_level:
                queue.append(next_level)
            res.append(curr_max)

        return res
