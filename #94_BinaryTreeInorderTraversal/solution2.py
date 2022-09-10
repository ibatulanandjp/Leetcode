'''
Iterative solution for Inorder traversal
'''

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        in_order_list = []
        stack = []

        while 1:

            # Push all the root left node to the stack
            while root:
                stack.append(root)
                root = root.left

            # Base condition (If stack is empty)
            if not stack:
                break

            # Pop and append the root (current) node to the inorder list
            root = stack.pop()
            in_order_list.append(root.val)

            # Move to the right nodes
            root = root.right

        return in_order_list

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
res = sol.inorderTraversal(n1)
print(res)
