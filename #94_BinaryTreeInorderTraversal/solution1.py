from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


# Recursive solution for Inorder traversal (left-Root-right)
# TC: O(n)
# SC: O(n)
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        inorder_list = []

        def dfs(root):
            if not root:
                return
            dfs(root.left)
            inorder_list.append(root.val)
            dfs(root.right)

        dfs(root)
        return inorder_list

n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
res = sol.inorderTraversal(n1)
print(res)
