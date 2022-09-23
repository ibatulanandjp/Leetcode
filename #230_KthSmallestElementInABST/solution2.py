from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        if not root:
            return None
        stack = []

        while True:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()

            # Decrement k to reach the Kth smallest element
            k -= 1
            if k == 0:
                return root.val

            root = root.right
