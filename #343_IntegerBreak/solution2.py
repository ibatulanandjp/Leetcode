# Method: Using Greedy Approach
# TC: O(n)
# SC: O(1)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        res = 1
        while n > 4:
            res *= 3
            n -= 3
        return res * n
