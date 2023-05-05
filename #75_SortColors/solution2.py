from typing import List


# Method: One-Pass
# Keep 3 pointers for each color, move along the list moving "red" to the left and "blue" to the right
# TC: O(n)
# SC: O(1)
class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red, white, blue = 0, 0, len(nums)-1

        while white <= blue:

            if nums[white] == 0:
                # Exchange nums[red] and nums[white]
                nums[red], nums[white] = nums[white], nums[red]
                red += 1
                white += 1

            elif nums[white] == 1:
                white += 1

            else:
                # Exchange nums[blue] and nums[white]
                nums[blue], nums[white] = nums[white], nums[blue]
                blue -= 1
