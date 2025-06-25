# Method: Recursive DFS with left and right bounds as arguments
# check if left < node.val < right for each node
# TC: O(n) where n is the number of nodes in the tree
# SC: O(n) for the recursion stack in the worst case (unbalanced tree)
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right) -> bool:
            if not node:
                return True
            if not (left < node.val < right):
                return False

            return valid(node.left, left, node.val) and valid(node.right, node.val, right)

        return valid(root, float('-inf'), float('inf'))