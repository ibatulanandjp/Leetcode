# Method: Calculate arithmetic sum for weeks (since each week's amount increases by 7)
# TC: O(1)
# SC: O(1)
class Solution:
    def totalMoney(self, n: int) -> int:
        full_weeks = n // 7
        first = 28
        last = 28 + (full_weeks - 1) * 7
        arithmetic_sum = full_weeks * (first + last) // 2

        monday = full_weeks + 1
        final_week = 0
        for day in range(n % 7):
            final_week += monday + day

        return arithmetic_sum + final_week