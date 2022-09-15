from typing import List

class Solution:
    def twoSum(self, nums:List[int], target: int) -> List[int] :
        seenMap={}
        for i in range(len(nums)) :
            remaining = target - nums[i]

            if remaining in seenMap : 
                return [seenMap[remaining], i]

            seenMap[nums[i]] = i

sol = Solution()
result = sol.twoSum([2,7,11,15], 9)
print(result)