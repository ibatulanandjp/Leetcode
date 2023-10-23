# Method: Use Logarithm (base10)
# TC: O(1)
# SC: O(1)

from math import log10


class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        return n > 0 and (log10(n) / log10(4)).is_integer()
