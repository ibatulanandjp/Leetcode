# Method: [Kadane's Algorithm] Calculate curr_sum by adding new num if it increases the sum,
# or reset it to current num if it doesn't, and update max_sum if curr_sum is greater than it.
# TC: O(n), since traversing the list only once
# SC: O(1), since no extra space is used
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum = nums[0]
        curr_sum = nums[0]

        for num in nums[1:]:    
            curr_sum = max(num, curr_sum + num)
            max_sum = max(max_sum, curr_sum)

        return max_sum                