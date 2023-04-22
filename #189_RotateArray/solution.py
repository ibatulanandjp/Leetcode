from typing import List

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # In case k > len(nums)
        k = k % len(nums)

        # Return if only 1 element in nums, or nothing to rotate
        if len(nums)<=1 or k==0:
            return

        # Reverse the list (MUST be nums[:] in LHS)
        nums[:] = nums[::-1]

        # Reverse the first part of the list (0...k)
        nums[:k] = nums[k-1::-1]

        # Reverse the second part of the list (k+1...n)
        nums[k:len(nums)] = nums[len(nums)-1:k-1:-1]