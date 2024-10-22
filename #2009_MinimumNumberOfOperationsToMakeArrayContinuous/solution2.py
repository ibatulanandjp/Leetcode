# Method: Use Sliding Window on sorted set of nums
# Traverse the set counting the difference
# TC: O(n logn)
# SC: O(n)
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))

        j = 0
        for i in range(len(new_nums)):
            while j < len(new_nums) and new_nums[j] < new_nums[i] + n:
                j += 1

            count = j - i
            ans = min(ans, n - count)

        return ans
