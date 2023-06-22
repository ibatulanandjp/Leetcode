from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# Method: DFS - Iterative (Inorder Traversal) -- Easy to understand (Common Format)
# Return when the Kth element is found in the Inorder traversal
# TC: O(n)
# SC: O(n)
def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
    count = 0
    stack = []

    while root or stack:
        if root:
            stack.append(root)
            root = root.left
        else:
            node = stack.pop()
            count += 1
            if count == k:
                return node.val
            root = node.right
    return -1
