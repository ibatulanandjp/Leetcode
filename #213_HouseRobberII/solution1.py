# Method: Dynamic Programming with 2 cases to handle circular arrangement 
# (1st + 3rd until last-1 or 2nd until last)
# TC: O(n), where n is the number of houses
# SC: O(1)
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0] + self.helper(nums[2:-1]), self.helper(nums[1:]))
    
    def helper(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0
        for n in nums:
            rob_new = max(rob1 + n, rob2)
            rob1 = rob2
            rob2 = rob_new
        return rob2