# Method: Sort and pair first and last element together
# TC: O(n logn), since we sort the elements
# SC: O(n), used for sorting (Tim sort)

from typing import List


class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        maxsum = 0
        for i in range(n//2):
            maxsum = max(maxsum, nums[i] + nums[n - i - 1])

        return maxsum