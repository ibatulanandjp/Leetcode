from typing import List

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(nums) == len(set(nums)):
            return False
        return True

sol = Solution()
print(sol.containsDuplicate([1, 3, 1, 2]))
