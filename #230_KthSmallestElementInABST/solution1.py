from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# Method: DFS - Inorder (Recursive)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        nodes = []
        self.dfs(root, nodes)
        # Return the Kth element from the Inorder List
        return nodes[k-1]

    # Function to get the Inorder List of the Tree
    def dfs(self, root: Optional[TreeNode], l: List[int]) -> None:
        if not root:
            return
        self.dfs(root.left, l)
        l.append(root.val)
        self.dfs(root.right, l)
