from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:

        def dnc(n):
            if len(n) == 0:
                return None
            mid = len(n) // 2
            root = TreeNode(n[mid])
            root.left = dnc(n[:mid])
            root.right = dnc(n[mid+1:])
            return root

        return dnc(nums)
