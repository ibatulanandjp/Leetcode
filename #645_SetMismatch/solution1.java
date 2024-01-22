// Method: Use set to find the sum of unique elements, and find the duplicate and missing element
// TC: O(n)
// SC: O(n)
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        
        // Calculate sum of numbers from 1...n
        int actualSum = n * (n + 1) / 2;
        
        // Calculate Array Sum
        int arraySum = 0;
        for (int num : nums) {
            arraySum += num;
        }

        // Calculate sum of unique elements in the set
        int uniqueSum = 0;
        Set<Integer> set = new HashSet<>();
        for (int num : nums) {
            set.add(num);
        }
        for (int num : set) {
            uniqueSum += num;
        }

        int duplicate = arraySum - uniqueSum;
        int missing = actualSum - uniqueSum;

        return new int[] {duplicate, missing};
    }
}