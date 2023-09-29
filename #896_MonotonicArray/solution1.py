# Method: Using flag to detect increasing and decreasing array
# Flag = 1: Increasing; Flag = -1: Decreasing; Flag = 0: Not Set or Equal values so far
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        flag = 0
        if len(nums) < 2:
            return True

        for i in range(1, len(nums)):
            if flag == 0:
                if nums[i] > nums[i-1]:
                    flag = 1
                elif nums[i] < nums[i-1]:
                    flag = -1
            else:
                if nums[i] >= nums[i-1] and flag == 1:
                    continue
                elif nums[i] <= nums[i-1] and flag == -1:
                    continue
                else:
                    return False

        return True
