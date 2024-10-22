# Method: Sort by using Custom Comparator
# TC: O(n*logn)
# SC: O(n)
from typing import List


class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        arr.sort(key=lambda num: (num.bit_count(), num)) # Sort again numerically if the num of bits are same
        return arr
