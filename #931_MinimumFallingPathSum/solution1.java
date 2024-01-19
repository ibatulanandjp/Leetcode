// Method: Use Dynamic Programming with memoization, and go on finding the minimum falling path
// TC: O(n^2)
// SC: O(1)

class Solution {
    public int minFallingPathSum(int[][] matrix) {
        int n = matrix.length;
        
        // Update the matrix with the min sum along the route
        for (int i = 1; i < n; i++) {
            for (int j = 0; j < n; j++) {
                matrix[i][j] += Math.min(matrix[i-1][Math.max(j-1, 0)],
                                        Math.min(matrix[i-1][j], 
                                            matrix[i-1][Math.min(j+1, n-1)]));
            }
        }

        // Find the minimum from the last row
        int minSum = Integer.MAX_VALUE;
        for (int num : matrix[n-1]) {
            minSum = Math.min(minSum, num);
        }
        return minSum;
    }
}