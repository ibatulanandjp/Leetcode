from typing import List

class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int] :
        seenMap={}
        for i, val in enumerate(nums) :
            remaining = target - nums[i]

            if remaining in seenMap : 
                return [seenMap[remaining], i]

            seenMap[val] = i

sol = Solution()
result = sol.twoSum([2,7,11,15], 9)
print(result)