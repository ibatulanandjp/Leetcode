from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        z_ptr, n_ptr = 0, 0

        while n_ptr < len(nums) and z_ptr < len(nums):

            # Not a zero
            if nums[z_ptr] != 0:
                z_ptr += 1

            # Not a number, or n_ptr is behind z_ptr
            elif nums[n_ptr] == 0 or n_ptr < z_ptr:
                n_ptr += 1

            # Swap
            else:
                nums[z_ptr] = nums[n_ptr]
                nums[n_ptr] = 0
