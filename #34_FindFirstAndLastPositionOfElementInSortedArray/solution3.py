# Method: Binary Search each for left and right (Optimized code for Solution2)
# Continue searching towards left for leftBias, and towards right for rightBias
# TC: O(logn)
# SC: O(1)
from typing import List


class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.binarySearch(nums, target, True)
        right = self.binarySearch(nums, target, False)
        return [left, right]

    # leftBias: [True/False], if false, res is rightBiased

    def binarySearch(self, nums: List[int], target: int, leftBias: bool) -> int:
        l, r = 0, len(nums) - 1
        index = -1

        while l <= r:
            m = (l + r) // 2

            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                index = m
                # Check bias condition, and continue searching
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1

        return index
