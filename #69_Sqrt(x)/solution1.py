# Method: Brute-force

class Solution:
    def mySqrt(self, x: int) -> int:
        res = 0 if x == 0 else 1
        for i in range(x):
            if i*i > x:
                res = i-1
                break
        return res
