from typing import List

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        result = 0
        # For each element in the list
        for n in nums:
            # XOR Rules:
            #   n XOR 0 = n
            #   n XOR n = 0
            # Perform XOR of element with result
            result ^= n
        return result