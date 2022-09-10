'''
Recursive solution for Inorder traversal
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root):
            if root:
                dfs(root.left)
                in_order_list.append(root.val)
                dfs(root.right)

        in_order_list = []
        dfs(root)
        return in_order_list


n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
res = sol.inorderTraversal(n1)
print(res)
