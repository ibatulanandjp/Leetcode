# Method: [Kadane's Algorithm] Calculate curr_max by adding new num, and update max_sum if curr_max is greater than it.
# TC: O(n), since traversing the list only once
# SC: O(1), since no extra space is used
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_max = nums[0]

        for num in nums[1:]:    
            curr_max = max(num, curr_max + num)
            max_sum = max(max_sum, curr_max)

        return max_sum                