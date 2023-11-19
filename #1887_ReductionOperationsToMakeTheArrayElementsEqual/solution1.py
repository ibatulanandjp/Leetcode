# Method: Sort and count operations with steps
# TC: O(n logn), since we perform sorting
# SC: O(n), required for Tim Sort
from typing import List


class Solution:
    def reductionOperations(self, nums: List[int]) -> int:
        nums.sort()
        ops, step = 0, 0

        for i in range(1, len(nums)):
            if nums[i] != nums[i-1]:
                step += 1
            ops += step
        return ops