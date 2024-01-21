// Method: Use Dynamic Programming and maintain max until the current element using previous 2 elements
// TC: O(n)
// SC: O(n)
class Solution {
    public int rob(int[] nums) {
        int n = nums.length;
        int[] dp = new int[n];

        if (n == 1) {
            return nums[0];
        } else if (n == 2) {
            return Math.max(nums[0], nums[1]);
        } else {
            dp[0] = nums[0];
            dp[1] = Math.max(nums[0], nums[1]);

            for (int i = 2; i < n; i++) {
                dp[i] = nums[i];
                dp[i] = Math.max(dp[i-1], dp[i-2] + dp[i]);
            }
            return dp[n-1];
        }
    }
}