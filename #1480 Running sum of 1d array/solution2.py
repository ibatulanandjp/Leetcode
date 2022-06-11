# NOTE: Commented codes are for local testing purpose only
# ---------------------------------------------------------
# from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        for i in range(1, len(nums)) : 
            nums[i] += nums[i-1]
        return nums

# sol = Solution()
# ans = sol.runningSum([1,2,3,4])
# print(ans)