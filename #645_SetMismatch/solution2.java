// Method: Use Hashmap for counting the occurrence of elements within 1...n 
// TC: O(n)
// SC: O(n)
class Solution {
    public int[] findErrorNums(int[] nums) {
        int n = nums.length;
        Map<Integer, Integer> map = new HashMap<>();

        for (int i = 1; i <= n; i++) {
            map.put(i, 1);
        }

        for (int num : nums) {
            map.put(num, map.get(num) - 1);
        }

        int duplicate = 0, missing = 0;
        for (Map.Entry<Integer, Integer> entry : map.entrySet()) {
            if (entry.getValue() == -1) {
                duplicate = entry.getKey();
            }
            if (entry.getValue() == 1) {
                missing = entry.getKey();
            }
        }

        return new int[]{duplicate, missing};
    }
}