// Method: Expand around center for odd and even length palindromes, counting palindromic substrings
// TC: O(n^2)
// SC: O(n)
class Solution {
    public int countSubstrings(String s) {
        int count = 0;
        for (int i = 0; i <= s.length(); i++) {
            count += expandAroundCenter(s, i, i);
            count += expandAroundCenter(s, i-1, i);
        }
        return count;
    }

    public int expandAroundCenter(String s, int l, int r) {
        int psCount = 0;
        char[] chars = s.toCharArray();
        while (l >= 0 && r < s.length() && chars[l] == chars[r]) {
            psCount++;
            l--;
            r++;
        }
        return psCount;
    }
}