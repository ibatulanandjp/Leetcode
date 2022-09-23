from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:    
        nodes = []
        self.dfs(root, nodes)
        return nodes[k-1]
        
        
    def dfs(self, root: Optional[TreeNode], l: List[int]) -> None:
        if root:
            self.dfs(root.left, l)
            l.append(root.val)
            self.dfs(root.right, l)        