// Method: Use dynamic programming, and traverse backwards to maintain a list of max within k elements
// TC: O(n * k)
// SC: O(n)
class Solution {
    public int maxSumAfterPartitioning(int[] arr, int k) {
        int n = arr.length;
        int dp[] = new int[n + 1];
        Arrays.fill(dp, 0);

        for (int start = n - 1; start >= 0; start--) {
            int currMax = 0;
            int end = Math.min(n, start + k);

            for (int i = start; i < end; i++) {
                currMax = Math.max(currMax, arr[i]);
                dp[start] = Math.max(dp[start], dp[i + 1] + currMax * (i - start + 1));
            }
        }
        return dp[0];
    }
}