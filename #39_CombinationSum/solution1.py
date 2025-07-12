# Method: Backtrack (DFS) to find all combinations using index of candidates
# Time Complexity: O(n^(t/m)), where n is the number of candidates, t is the target, and m is the minimum candidate value.
# Space Complexity: O(t/m)
from typing import List

class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()

        def dfs(i, current, total):
            if total == target:
                res.append(current.copy())
                return
            
            for j in range(i, len(nums)):
                if total + nums[j] > target:
                    return
                current.append(nums[j])
                dfs(j, current, total + nums[j])
                current.pop()

        dfs(0, [], 0)
        return res
        
