from typing import List


class Solution:
    def maximumSubarray(self, nums: List[int]) -> int:
        maxSumSoFar = nums[0]
        currentMax = 0

        for i in range(0, len(nums)):

            currentMax = currentMax + nums[i]

            # print("Current Max: ", currentMax)
            # print("MaxSumSoFar: ", maxSumSoFar)

            if maxSumSoFar < currentMax :
                maxSumSoFar = currentMax

            if currentMax < 0:
                currentMax = 0

        return maxSumSoFar


sol = Solution()
print(sol.maximumSubarray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))    #6
# print(sol.maximumSubarray([5, 4, -1, 7, 8]))    #23
# print(sol.maximumSubarray([-2,1]))  #1
# print(sol.maximumSubarray([-1]))    #-1
# print(sol.maximumSubarray([-2, -1]))    #-1
# print(sol.maximumSubarray([-3,-2,0,-1]))    #0
