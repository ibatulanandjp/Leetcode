# Method: Sort the nums, and compare adjacent nums
# TC: O(n)
# SC: O(1)
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(len(nums)-1):
            if(nums[i] == nums[i+1]):
                return True
        return False