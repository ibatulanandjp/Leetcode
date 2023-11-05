# Method: Convert into set and compare length
# TC: O(1)
# SC: O(1)
from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums) != len(set(nums))