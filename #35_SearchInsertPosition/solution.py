# Method: Binary Search; with +1 if nums[mid] is less than target
# TC: O(log n)
# SC: O(1)
from typing import List


class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        result = 0

        while left <= right:
            mid = left + (right-left) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                result = mid + 1
                left = mid + 1
            else:
                result = mid
                right = mid - 1
        return result
