from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        while root:
            if p.val < root.val > q.val:
                root = root.left
            elif p.val > root.val < q.val:
                root = root.right
            else:
                return root

n1 = TreeNode(6)
n2 = TreeNode(2)
n3 = TreeNode(8)
n4 = TreeNode(0)
n5 = TreeNode(4)
n6 = TreeNode(7)
n7 = TreeNode(9)


n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

sol = Solution()
res = sol.lowestCommonAncestor(n1, n2, n3)
print(res.val)
