from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None) -> None:
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        def invert(node):
            if not node:
                return
            temp = node.left
            node.left = node.right
            node.right = temp

            if node.left:
                invert(node.left)
            if node.right:
                invert(node.right)


        node = root
        invert(node)
        return node

    # Utility Function just for printing the tree in level-order
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        level_order_list = []
        queue = []

        # If there's no root
        if not root:
            return level_order_list

        # Add the root node to the queue
        queue.append([root])

        # While queue is not empty
        while queue:

            # Pop the level-wise element from the queue
            curr_level = queue.pop(0)
            level_list = []
            next_level = []

            # For each node in the current level
            for node in curr_level:
                # print(node.val)

                # Append the node value
                level_list.append(node.val)

                # Append node's left and right
                if node.left:
                    next_level.append(node.left)
                if node.right:
                    next_level.append(node.right)

            # Append level-wise node list to the queue
            if next_level:
                queue.append(next_level)
            
            # Append level-wise node values to the list
            level_order_list.append(level_list)

        return level_order_list

n1 = TreeNode(4)
n2 = TreeNode(2)
n3 = TreeNode(7)
n4 = TreeNode(1)
n5 = TreeNode(3)
n6 = TreeNode(6)
n7 = TreeNode(9)

n1.left = n2
n1.right = n3
n2.left = n4
n2.right = n5
n3.left = n6
n3.right = n7

sol = Solution()
res = sol.invertTree(n1)

print(sol.levelOrder(res))
