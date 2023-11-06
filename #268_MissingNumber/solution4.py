# Method: Using Bitwise XOR (Rules: a^a=0 and a^0=a)
# TC: O(n)
# SC: O(1)

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        s = 0
        # Calculate XOR with all the nums elements
        for i in range(len(nums)):
            s ^= nums[i]
        # Then, Calculate XOR with all the numbers within the length
        for i in range(1, len(nums)+1):
            s ^= i
        return s
