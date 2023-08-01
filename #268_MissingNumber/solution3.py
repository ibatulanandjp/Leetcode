# Method: Using Maths (sum = n(n+1)/2)
# TC: O(n)
# SC: O(1)

from typing import List

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        sum_n = (n * (n + 1 )) // 2

        sum_nums = 0
        for n in nums:
            sum_nums += n

        return sum_n - sum_nums