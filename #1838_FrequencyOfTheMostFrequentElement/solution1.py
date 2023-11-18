# Method: Use Sliding window, calculating sum of all elements within the window and comparing with "k"
# TC: O(n logn), since we sort the nums.
# SC: O(n), since we use Tim sort for sorting.
from typing import List


class Solution:
    def maxFrequency(self, nums: List[int], k: int) -> int:
        nums.sort()
        res, curr = 0, 0
        
        l = 0
        for r in range(len(nums)):
            target = nums[r]
            curr += target

            while (r - l + 1) * target - curr > k:
                curr -= nums[l]
                l += 1
            
            res = max(res, r - l + 1)
        
        return res