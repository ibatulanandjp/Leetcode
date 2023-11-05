# Method: Use 2-pass (left-right and right-left)
# Calculate resultant by multiplying number with all before it
# TC: O(n), since only 2 passes
# SC: O(1), since no extra space (apart from result)
from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        # Left to right
        for i in range(1, len(nums)):
            res[i] = res[i-1] * nums[i-1]
        
        # Right to left
        right = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= right
            right *= nums[i]

        return res