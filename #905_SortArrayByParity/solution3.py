# Method: Using python list comprehension
# TC: O(n)
# SC: O(n)
from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        return [x for x in nums if x % 2 == 0] + [x for x in nums if x % 2 == 1]
