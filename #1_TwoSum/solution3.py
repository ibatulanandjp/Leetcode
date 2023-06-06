# TC: O(n)
# SC: O(n)
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Map to store remaining number
        seen_map = {}

        for i, n in enumerate(nums):
            # Remaining number to find
            remaining = target - n

            # If remaining number was seen already, return the indices
            if remaining in seen_map:
                return [seen_map.get(remaining), i]

            # (Else) Add the index to the seen map
            seen_map[n] = i
