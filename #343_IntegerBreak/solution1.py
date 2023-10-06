# Method: Mathematical approach
# TC: O(1)
# SC: O(1)
class Solution:
    def integerBreak(self, n: int) -> int:
        if n <= 3:
            return n-1

        quo = n // 3
        rem = n % 3
        if rem == 0:
            return 3 ** quo
        elif rem == 1:
            return 3 ** (quo - 1) * 4
        else:
            return 3 ** quo * 2
