// Method: Sort the array and check for condition within 3 elements at a time
// TC: O(n logn), for sorting
// SC: O(log n), used in sorting (Java's Arrays.sort uses Quicksort)
class Solution {
    public int[][] divideArray(int[] nums, int k) {
        Arrays.sort(nums);
        int[][] res = new int[nums.length / 3][3];

        for (int i = 0; i < nums.length; i += 3) {
            if (nums[i + 2] - nums[i] > k) {
                return new int[0][0];
            }
            res[i / 3] = new int[]{nums[i], nums[i + 1], nums[i + 2]};
        }
        return res;
    }
}