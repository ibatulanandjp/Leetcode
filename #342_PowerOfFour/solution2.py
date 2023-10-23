# Method: Use Logarithm (base2) since, 4^x = 2^2x
# TC: O(1)
# SC: O(1)

from math import log2, sqrt


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and log2(sqrt(n)).is_integer()
