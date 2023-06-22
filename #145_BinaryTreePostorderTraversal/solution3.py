from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res, stack = [], []
        while root or stack:
            if root:
                res.append(root.val)
                stack.append(root)
                root = root.right
            else:
                node = stack.pop()
                root = node.left
        return res[::-1]
    
n1 = TreeNode(1)
n2 = TreeNode(2)
n3 = TreeNode(3)

n1.right = n2
n2.left = n3

sol = Solution()
res = sol.postorderTraversal(n1)
print(res)