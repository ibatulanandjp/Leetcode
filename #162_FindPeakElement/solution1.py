from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        
        nums.append(float('-inf'))
        nums.append(float('-inf'))
        
        for i in range(0, len(nums)-2):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                return i