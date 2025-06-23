# Method: DFS Recursive with Max Function
# TC: O(n) - where n is the number of nodes in the tree
# SC: O(h) - where h is the height of the tree (call stack depth)
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))