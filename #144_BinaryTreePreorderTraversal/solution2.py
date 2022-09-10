'''
Iterative solution for preorder traversal
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
    
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        pre_order_list = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                pre_order_list.append(node.val)
                # Since it's a stack, which is LIFO, the order of appending gets reversed [i.e. Right then Left]
                stack.append(node.right)
                stack.append(node.left)
        return pre_order_list


n1 = TreeNode(3)
n2 = TreeNode(1)
n3 = TreeNode(2)

n1.left = n2
n1.right = n3

sol = Solution()
res = sol.preorderTraversal(n1)
print(res)