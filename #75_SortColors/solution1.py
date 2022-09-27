from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = 0
        
        for i in range(len(nums)):
            if nums[i] == 0:
                red += 1
            elif nums[i] == 1:
                white += 1
            else:
                blue += 1

        for i in range(red):
            nums[i]=0
        for i in range(red, red+white):
            nums[i]=1
        for i in range(red+white, len(nums)):
            nums[i]=2