from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:

        if not root:
            return False

        '''
        The stack should keep both node and node.val, 
        since the intermediate sum needs to be reverted back
        in case the it exceeds the targetSum
        '''
        stack = [(root, root.val)]

        while stack:
            node, nodeVal = stack.pop()
            print("Node:", nodeVal)

            # If the intermediate sum == targetSum and it's a leaf node
            if nodeVal == targetSum and node.left is None and node.right is None:
                return True

            # Push right node with updated intermediate sum
            if node.right:
                stack.append((node.right, nodeVal+node.right.val))
            # Push left node with updated intermediate sum
            if node.left:
                stack.append((node.left, nodeVal+node.left.val))

        return False


n1 = TreeNode(5)
n2 = TreeNode(4)
n3 = TreeNode(8)
n4 = TreeNode(11)
n5 = TreeNode(13)
n6 = TreeNode(4)
n7 = TreeNode(7)
n8 = TreeNode(2)
n9 = TreeNode(1)

n1.left = n2
n1.right = n3
n2.left = n4
n3.left = n5
n3.right = n6
n4.left = n7
n4.right = n8
n6.right = n9

sol = Solution()
res = sol.hasPathSum(n1, 22)
print(res)
