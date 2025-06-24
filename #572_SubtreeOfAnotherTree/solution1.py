# Method: DFS Iterative - use sameTree helper function
# and compare the current node with subRoot, to start the comparison
# TC: O(m * n) where m is the number of nodes in root and n is the number of nodes in subRoot
# SC: O(m + n) for the stack space used in the worst case
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:        
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                if node.val == subRoot.val:
                    res = self.sameTree(node, subRoot)
                    if res: return True
                stack.append(node.left)
                stack.append(node.right)

        return False


    def sameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
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