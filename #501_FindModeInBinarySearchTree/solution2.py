# Method: Use Inorder Traversal with 
# TC: O(n)
# SC: O(1), if the stack is ignored, else O(n) including stack

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:

        def dfs(node):
            nonlocal max_count, curr_count, prev_num, res
            if not node:
                return

            dfs(node.left)

            curr_num = node.val
            if curr_num == prev_num:
                curr_count += 1
            else:
                curr_count = 1
                prev_num = curr_num

            if curr_count > max_count:
                res = []
                max_count = curr_count
            if curr_count == max_count:
                res.append(curr_num)

            dfs(node.right)

        curr_count = 0
        max_count = 0
        prev_num = 0
        res = []
        dfs(root)
        return res
