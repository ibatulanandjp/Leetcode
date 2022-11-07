from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # Initialize LIS array with 1 for all nums
        LIS = [1 for i in nums]

        # Iterate backwards from the end of the nums list
        for i in range(len(nums)-1, -1, -1):

            # From i+1 till the end of the list
            for j in range(i+1, len(nums)):

                # If the current num is less than the later
                if nums[i] < nums[j]:
                    # Update the LIS of current num
                    LIS[i] = max(LIS[i], LIS[j]+1)

        return max(LIS)
