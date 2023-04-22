from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Sort the list
        nums.sort()

        # For each element, incremented with 2
        for i in range(0, len(nums)-1, 2):
            # If elements at i and i+1 doesn't match, it's the "Single Number"
            if nums[i] != nums[i+1]:
                return nums[i]
        # Return the last element
        return nums[len(nums)-1]