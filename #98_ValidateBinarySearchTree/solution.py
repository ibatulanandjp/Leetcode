from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode], floor=float("-inf"), ceiling=float("inf")) -> bool:
        if not root:
            return True
        if root.val <= floor or root.val >= ceiling:
            return False
        return self.isValidBST(root.left, floor, root.val) and \
            self.isValidBST(root.right, root.val, ceiling)


n1 = TreeNode(4)
n2 = TreeNode(5)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5

sol = Solution()
res = sol.isValidBST(n1)
print(res)
