from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Method: DFS - Iterative (Inorder Traversal)
# Return when the Kth element is found in the Inorder traversal
# TC: O(n)
# SC: O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        # To keep track of the Kth smallest element
        n = 0
        stack = []
        current = root

        while current or stack:
            # [left]
            while current:
                stack.append(current)
                current = current.left

            # [Root]
            current = stack.pop()
            n += 1
            if n == k:
                return current.val

            # [right]
            current = current.right
