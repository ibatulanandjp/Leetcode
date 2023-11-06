# Method: Use Dynamic Programming and Bit manipulation to count no. of 1's
# TC: O(n), where n is the number, to iterate through the numbers from 1 to n+1 
# SC: O(n), for output array
from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0] * (n + 1)
        for i in range(1, n + 1):
            # i >> 1 is i//2 and it should find the half of i, which has similar no. of 1's (DP way to lookup already calculated value)
            # i & 1 is i%2 and it checks the last bit 
            res[i] = res[i >> 1] + (i & 1)
        return res
