from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:

        if not root:
            return False

        # Recursive Function to find compliment and check if that exist in the set or not 
        def _findTarget(node, nodes, k):

            if not node:
                return False

            # Find compliment, and check in nodes set
            compliment = k - node.val
            if compliment in nodes:
                return True

            # If compliment not in nodes set, add it to the set
            nodes.add(node.val)

            # Recursive call for left and right nodes, return OR of both
            return _findTarget(node.left, nodes, k) or _findTarget(node.right, nodes, k)

        return _findTarget(root, set(), k)


n1 = TreeNode(5)
n2 = TreeNode(3)
n3 = TreeNode(6)
n4 = TreeNode(2)
n5 = TreeNode(4)
n6 = TreeNode(7)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.right = n6

sol = Solution()
res = sol.findTarget(n1, 4)
print(res)
