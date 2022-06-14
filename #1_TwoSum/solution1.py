from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int] :
        for i in range(len(nums)-1) :
            for j in range(i+1, len(nums)) :
                if nums[i]+nums[j]==target :
                    return [i,j]

sol = Solution()
result = sol.twoSum([2,7,11,15], 9)
print(result)