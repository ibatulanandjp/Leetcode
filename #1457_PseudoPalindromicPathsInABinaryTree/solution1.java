// Method: Use preorder traversal to find all the paths,
// and in the due course, check for digit frequency using bit manipulation
// TC: O(n)
// SC: O(h), where h is the height of the tree

/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public int pseudoPalindromicPaths (TreeNode root) {
        return preorder(root, 0);
    }

    public int preorder(TreeNode node, int path) {
        if (node == null) {
            return 0;
        }

        // Compute occurrence of each digit
        path = path ^ (1 << node.val);
        // If it's a leaf node, check if the path is pseudo palidromic
        if (node.left == null && node.right == null) {
            // Check if at most one digit has an odd frequency
            return (path & (path - 1)) == 0 ? 1 : 0;
        }
        return preorder(node.left, path) + preorder(node.right, path);
    }
}