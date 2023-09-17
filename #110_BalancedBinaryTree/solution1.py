# Method: Use Recursive method to find height of left and right subtree at each node
# TC: O(n), where n is no. of nodes in the tree
# SC: O(n), for recursive call stack
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        if abs(self.getHeight(root.left) - self.getHeight(root.right)) <= 1:
            return self.isBalanced(root.left) and self.isBalanced(root.right)
        return False

    def getHeight(self, root: Optional[TreeNode]) -> int:
        return 1 + max(self.getHeight(root.left), self.getHeight(root.right)) if root else 0
