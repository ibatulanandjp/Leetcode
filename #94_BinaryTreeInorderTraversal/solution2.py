from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


# Iterative solution for Inorder traversal (left-Root-right)
# TC: O(n)
# SC: O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:

        in_order_list = []
        stack = []
        current = root

        while current or stack:
            # [left] Push to the stack and keep moving to the left till current is None
            while current:
                stack.append(current)
                current = current.left

            # [Root] Pop and append to the result
            current = stack.pop()
            in_order_list.append(current.val)

            # [right] Move right
            current = current.right
        return in_order_list

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
res = sol.inorderTraversal(n1)
print(res)
