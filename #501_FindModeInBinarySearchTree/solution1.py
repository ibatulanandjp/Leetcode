# Method: Use Hashmap to store max count of node
# TC: O(n)
# SC: O(n)

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        node_count = defaultdict(int)
        stack = [root]

        # Traverse the tree, counting the node frequency
        while stack:
            node = stack.pop()
            node_count[node.val] += 1

            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)

        # Create a resultant list with node of max count
        res = []
        max_count = 0
        for k, v in node_count.items():
            if v == max_count:
                res.append(k)
            elif v > max_count:
                res = [k]
                max_count = v

        return res
