# Method: Use two-pointers to maintain positive and negative index
# TC: O(n)
# SC: O(n)
from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        res = [0] * len(nums)
        pos_index, neg_index = 0, 1
        
        for i in range(len(nums)):
            if nums[i] > 0:
                res[pos_index] = nums[i]
                pos_index += 2
            else:
                res[neg_index] = nums[i]
                neg_index += 2
        return res