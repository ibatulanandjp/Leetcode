# Method: Dynamic Programming (Space Optimized) while checking only last two robbed amounts
# TC: O(n), where n is the number of houses
# SC: O(1), since we are using only two variables to store the last two robbed amounts
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        for n in nums:
            new_rob = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = new_rob
        return rob2