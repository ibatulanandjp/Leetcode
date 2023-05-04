from typing import List


# Method: Backtracking (Recursive) Bottom-to-Top
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        
        # Base Case
        if len(nums) == 1:
            return [nums[:]]
        
        result = []
        for i in range(len(nums)):
            remaining = nums[:i] + nums[i+1:]
            perms = self.permute(remaining)
            for perm in perms:
                result.append([nums[i]] + perm)
        
        return result
            