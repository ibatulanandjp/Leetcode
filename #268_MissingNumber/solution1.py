# Method: Naive approach
# TC: O(n^2)
# SC: O(1)

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = None
        for i in range(len(nums)):
            if i not in nums:
                res = i
        return res if res != None else len(nums)
