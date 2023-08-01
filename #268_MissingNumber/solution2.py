# Method: Using HashMap (Counter)
# TC: O(n)
# SC: O(n)

from typing import List
from collections import Counter


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        count = Counter(nums)
        for i in range(len(nums)+1):
            if not count.get(i):
                return i
