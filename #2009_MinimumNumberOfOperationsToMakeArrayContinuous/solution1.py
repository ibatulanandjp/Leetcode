# Method: Use Binary Search on sorted set of nums
# Then, find left and right for each element
# TC: O(n logn)
# SC: O(n)
from typing import List
from bisect import bisect_right


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)
        ans = n
        new_nums = sorted(set(nums))

        for i in range(len(new_nums)):
            left = new_nums[i]
            right = left + n - 1
            j = bisect_right(new_nums, right)
            count = j - i
            ans = min(ans, n - count)
        return ans
