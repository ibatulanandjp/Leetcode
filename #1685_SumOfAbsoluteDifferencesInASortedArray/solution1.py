# Method: Calculate PrefixSum and SuffixSum on the fly
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0
        ans = []

        for i in range(len(nums)):
            right_sum = total_sum - left_sum - nums[i]

            left_total = (nums[i] * i) - left_sum
            right_total = right_sum - (nums[i] * (n-i-1))

            ans.append(left_total + right_total)
            left_sum += nums[i]

        return ans
