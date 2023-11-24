# Method: Sort and add all the alternate nums from the end (using left and right ptrs)
# TC: O(n logn), required for sorting
# SC: O(n), required for Tim Sort
from typing import List


class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        res = 0
        l, r = 0, len(piles)
        while l < r:
            r -= 2
            l += 1
            res += piles[r]
        return res
