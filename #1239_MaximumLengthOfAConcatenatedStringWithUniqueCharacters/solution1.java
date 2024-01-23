// Method: Use DFS
// TC: O(2^n)
// SC: O(n)
class Solution {
    private int result = 0;

    public int maxLength(List<String> arr) {
        dfs(arr, "", 0);
        return result;
    }

    private void dfs(List<String> arr, String currString, int index) {
        boolean unique = isUniqueChar(currString);
        // If unique characters, then update result with max
        if(unique) {
            result = Math.max(result, currString.length());
        }

        // Base case for recursion
        if(index == arr.size() || !unique) {
            return;
        }

        // Recusively call dfs with next element
        for(int i = index; i < arr.size(); i++) {
            dfs(arr, currString + arr.get(i), i + 1);
        }
    }

    // Function to check if all the characters in a string is unique
    private boolean isUniqueChar(String s) {
        Set<Character> charset = new HashSet<>();
        for(char ch : s.toCharArray()) {
            if(charset.contains(ch)) {
                return false;
            }
            charset.add(ch);
        }
        return true;
    }
}