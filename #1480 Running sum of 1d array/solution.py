# NOTE: Commented codes are for local testing purpose only
# ---------------------------------------------------------
# from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sumList: List[int] = []
        sum = 0
        for i in nums : 
            sum+=i
            sumList.append(sum)
        return sumList

# sol = Solution()
# ans = sol.runningSum([1,2,3,4])
# print(ans)