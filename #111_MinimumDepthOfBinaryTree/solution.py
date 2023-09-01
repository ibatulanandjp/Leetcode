# Method: Use DFS; Handle cases when only left or right child exist
# If either left or right is empty, return 1+left+right, else return 1+min(left, right)
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
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        leftDepth = self.minDepth(root.left)
        rightDepth = self.minDepth(root.right)

        # If left or right subtree is empty, return sum of left and right, by adding 1
        if leftDepth == 0 or rightDepth == 0:
            return 1 + leftDepth + rightDepth

        # Else, return min of left and right, by adding 1
        return 1 + min(leftDepth, rightDepth)
