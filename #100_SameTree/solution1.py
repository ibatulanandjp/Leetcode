# Method: DFS Iterative - with 1 stack storing (node1, node2) pairs
# TC: O(n) - where n is the number of nodes in the trees
# SC: O(n) - for the stack used to store pairs of nodes
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        stack = [(p, q)]

        while stack:
            node1, node2 = stack.pop()
            
            if not node1 and not node2:
                continue
            if not node1 or not node2 or node1.val != node2.val:
                return False
            stack.append((node1.left, node2.left))
            stack.append((node1.right, node2.right))

        return True
