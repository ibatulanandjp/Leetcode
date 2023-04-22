from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Variable to count of unique elements in the list
        unique_count = 1

        # For every element in the list
        for i in range(len(nums)-1):
            if nums[i] != nums[i+1]:
                # Replace the element at unique_count with the new unique element found in the list
                nums[unique_count] = nums[i+1]
                # Increment the unique_count
                unique_count += 1
        return unique_count