# Method: DFS with Post-order Traversal to check max path sum at each node
# TC: O(n), where n is the number of nodes in the tree
# SC: O(n), for recursion stack
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        
        def dfs(root) -> int:
            if not root:
                return 0
            
            # NB: Consider only positive (> 0) contributions from left and right children
            l_max = max(dfs(root.left), 0)
            r_max = max(dfs(root.right), 0)

            nonlocal max_sum
            max_sum = max(max_sum, r_max + l_max + root.val)
            return root.val + max(r_max, l_max)


        max_sum = root.val
        dfs(root)
        return max_sum