# Method: Use modified Binary Search to find the minimum element
# TC: O(log n)
# SC: O(1)
from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            
            if nums[m] > nums[r]:
                l = m + 1
            else:
                r = m
                
        return nums[l]