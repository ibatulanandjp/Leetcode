// Method: Use HashMap
// TC: O(m^2 * n)
// SC: O(m)
class Solution {
    public int numSubmatrixSumTarget(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;
        int result = 0;

        // Calculate prefix sum for each row
        for (int i = 0; i < row; i++) {
            for (int j = 1; j < col; j++) {
                matrix[i][j] += matrix[i][j - 1];
            }
        }

        // For each pair of column, find the subarray sum which is equal to target
        for (int c1 = 0; c1 < col; c1++) {
            for (int c2 = c1; c2 < col; c2++) {
                Map<Integer, Integer> map = new HashMap<>();
                map.put(0, 1);

                int sum = 0;
                for (int r = 0; r < row; r++) {
                    sum += matrix[r][c2];
                    if (c1 > 0) {
                        sum -= matrix[r][c1 - 1];
                    }
                    result += map.getOrDefault(sum - target, 0);
                    map.put(sum, map.getOrDefault(sum, 0) + 1);
                }
            }
        }
        return result;
    }
}