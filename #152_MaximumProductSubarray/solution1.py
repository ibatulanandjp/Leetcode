# Method: [Kadane's Algorithm] Calculate curr_max and curr_min, and update max_prod if curr_max is greater than it.
# Important factor is to consider that -ve value can also yield a maximum product, if another -ve value is found.
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min, curr_max = nums[0], nums[0]
        max_prod = nums[0]
        
        for num in nums[1:]:
            temp_max = curr_max
            # Calculate curr_max and curr_min
            curr_max = max(num, curr_max*num, curr_min*num)
            curr_min = min(num, temp_max*num, curr_min*num)

            # Calculate max_prod
            max_prod = max(max_prod, curr_max)

        return max_prod