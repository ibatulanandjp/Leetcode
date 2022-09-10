'''
Recursive solution for preorder traversal
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(root: Optional[TreeNode]):
            if not root:
                return
            pre_order_list.append(root.val)
            dfs(root.left)
            dfs(root.right)

        pre_order_list = []
        dfs(root)
        return pre_order_list

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
res = sol.preorderTraversal(n1)
print(res)