# Method: Use Hashmap with factorial method to select 2 from the count, and add all to find the result
# TC: O(n * m), where n is length of nums, m is nums
# SC: O(n)
from collections import Counter
from typing import List
from math import factorial


class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        res = 0
        count_map = Counter(nums)
        for key, val in count_map.items():
            if val > 1:
                res += factorial(val) // (factorial(val-2) * factorial(2))
        return res
