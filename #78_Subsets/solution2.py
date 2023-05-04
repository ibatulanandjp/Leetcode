from typing import List


# Method: Backtrack (Recursive)
# For each element in the list, choose either:
#   1: To include it in the subset
#   2: NOT to include it in the subset
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        res = []
        subset = []

        def backtrack(i):
            # Base Case: Last element is reached
            if i >= len(nums):
                res.append(subset[:])
                return

            # Decision to include nums[i]
            subset.append(nums[i])
            backtrack(i + 1)

            # Decision NOT to include nums[i]
            subset.pop()
            backtrack(i + 1)

        backtrack(0)
        return res
