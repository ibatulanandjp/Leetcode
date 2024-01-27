// Method: Use Dynamic Programming (2D) to calculate count of permutations with inverse pair
// TC: O(n*k)
// SC: O(n*k)
class Solution {
    public int kInversePairs(int n, int k) {
        final int MOD = 1_000_000_007;
        // Store count of permutations with length i, with j inverse pair
        int[][] dp = new int[n + 1][k + 1];
        
        // Base case initialization
        for (int i = 0; i <= n; i++)
            dp[i][0] = 1;

        for (int i = 1; i <= n; i++) {
            for (int j = 1; j <= k; j++) {
                dp[i][j] = (dp[i][j - 1] + dp[i - 1][j]) % MOD;
                if (j >= i) {
                    // + MOD, since MOD is already taken, so it might go into -ve value for some test cases
                    dp[i][j] = (dp[i][j] - dp[i - 1][j - i] + MOD) % MOD;
                }
            }
        }
        return dp[n][k];
    }
}