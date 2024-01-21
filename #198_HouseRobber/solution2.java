// Method: Use space optimized Dynamic Programming approach, using previous 2 max robbery amounts
// TC: O(n)
// SC: O(1)
class Solution {
    public int rob(int[] nums) {
        int rob = 0;
        int noRob = 0;
        for (int i = 0; i < nums.length; i++) {
            int newRob = noRob + nums[i];
            int newNoRob = Math.max(noRob, rob);
            rob = newRob;
            noRob = newNoRob;
        }
        return Math.max(rob, noRob);
    }
}