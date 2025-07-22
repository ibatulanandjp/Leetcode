# Method: Dynamic Programming (space optimized) to check only last 2 steps
# TC: O(n), where n is the number of steps
# SC: O(1), only constant space is used
class Solution:
    def climbStairs(self, n: int) -> int:
        res = 1
        two_before = 1
        one_before = 1
        for i in range(2, n+1):
            res = one_before + two_before
            two_before = one_before
            one_before = res
        return res
