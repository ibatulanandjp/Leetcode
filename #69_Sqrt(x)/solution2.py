# Method: Binary Search

class Solution:
    def mySqrt(self, x: int) -> int:
        first = 0 if x == 0 else 1
        last = x
        while first <= last:
            mid = first + (last-first) // 2
            if mid*mid == x:
                return mid
            elif mid*mid > x:
                last = mid-1
            else:
                first = mid+1
        return last
