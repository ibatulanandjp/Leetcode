'''
Iterative solution for Postorder traversal
'''
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        post_order_list = []
        stack = [root]

        while stack:
            node = stack.pop()
            if node:
                stack.append(node.left)
                stack.append(node.right)
                post_order_list.append(node.val)            

        # Return reversed list for post order
        return post_order_list[::-1]

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
res = sol.postorderTraversal(n1)
print(res)
