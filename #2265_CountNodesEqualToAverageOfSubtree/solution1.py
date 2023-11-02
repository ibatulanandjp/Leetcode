# Method: Use Postorder traversal with (sum, count) passing to the next level
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
    def averageOfSubtree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def traverse(node):
            nonlocal result

            if not node:
                return 0, 0

            l_sum, l_count = traverse(node.left)
            r_sum, r_count = traverse(node.right)

            curr_sum = node.val + l_sum + r_sum
            curr_count = 1 + l_count + r_count

            if curr_sum // curr_count == node.val:
                result += 1

            return curr_sum, curr_count

        traverse(root)
        return result