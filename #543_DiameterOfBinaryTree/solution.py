# Method: Use DFS; calculate depth of left and right subtree, and update diameter with max
# TC: O(n)
# SC: O(n)
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.depth(root)
        return self.diameter

    def depth(self, node: Optional[TreeNode]) -> int:
        if not node:
            return 0
        leftDepth = self.depth(node.left)
        rightDepth = self.depth(node.right)

        self.diameter = max(self.diameter, leftDepth + rightDepth)
        return 1 + max(leftDepth, rightDepth)
