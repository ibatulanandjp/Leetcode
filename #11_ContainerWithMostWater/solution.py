# Method: Two pointers
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_water = 0
        left, right = 0, len(height)-1

        while left <= right:
            curr_water = (right-left) * min(height[right], height[left])
            max_water = max(max_water, curr_water)

            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return max_water
