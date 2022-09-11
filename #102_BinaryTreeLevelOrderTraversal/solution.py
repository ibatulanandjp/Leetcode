from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
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


n1 = TreeNode(3)
n2 = TreeNode(9)
n3 = TreeNode(20)
n4 = TreeNode(15)
n5 = TreeNode(7)

n1.left = n2
n1.right = n3
n3.left = n4
n3.right = n5

sol = Solution()
res = sol.levelOrder(n1)
print(res)
