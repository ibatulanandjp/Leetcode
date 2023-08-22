# Method: Using Hashmap
# TC: O(n)
# SC: O(n)

from typing import List
from collections import defaultdict


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count = defaultdict(int)
        for n in nums:
            count[n] += 1
            if count[n] > len(nums)//2:
                return n
        return 0
