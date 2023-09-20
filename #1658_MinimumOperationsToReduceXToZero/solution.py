# Method: Use Sliding Window (2 pointers)
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def minOperations(self, nums: List[int], x: int) -> int:
        target = sum(nums) - x
        n = len(nums)

        if target == 0:
            return n

        max_len = curr_sum = left = 0
        for right, val in enumerate(nums):
            curr_sum += val
            while left <= right and curr_sum > target:
                curr_sum -= nums[left]
                left += 1
            if curr_sum == target:
                max_len = max(max_len, right - left + 1)

        return n - max_len if max_len else -1
