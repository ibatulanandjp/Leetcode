// Method: Traverse in reverse order, and whenever the char is an odd number, the largest odd number is found
// TC: O(n)
// SC: O(1)
class Solution {
    public String largestOddNumber(String num) {
        for (int i = num.length()-1; i >= 0; i--) {
            if((int)(num.charAt(i)) % 2 != 0) {
                return num.substring(0, i + 1);
            }
        }
        return "";
    }
}