// Method: Calculate arithmetic sum for weeks (since each week's amount increases by 7)
// TC: O(1)
// SC: O(1)
class Solution {
    public int totalMoney(int n) {
        int fullWeeks = n / 7;
        int first = 28;
        int last = 28 + (fullWeeks - 1) * 7;
        int arithmeticSum = fullWeeks * (first + last) / 2;

        int monday = 1 + fullWeeks;
        int finalWeek = 0;
        for (int day = 0; day < n % 7; day++) {
            finalWeek += monday + day;
        }

        return arithmeticSum + finalWeek;
    }
}