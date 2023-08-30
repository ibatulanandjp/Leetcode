# Method: Use 2 pointers to swap the 'val' from left to right
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        if not nums:
            return -1
        left, right = 0, len(nums)-1
        while left < right:
            if nums[left] == val:
                nums[left], nums[right] = nums[right], nums[left]
                right -= 1
            else:
                left += 1
        return left+1 if nums[left] != val else left
