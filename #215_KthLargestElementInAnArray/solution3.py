# Method: Using Quick find method (A method similar to Quick sort)
# Gives better Average Case time complexity
# TC: Average: O(n), Worst: O(n^2)
# SC: Average: O(logn), Worst: O(n) 
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # For easier calculation, update k
        k = len(nums) - k

        def quickSelect(l: int, r: int) -> int:
            pivot, p = nums[r], l

            for i in range(l, r):
                if nums[i] <= pivot:
                    # Swap nums[p] with nums[i]
                    nums[i], nums[p] = nums[p], nums[i]
                    p += 1
            # Swap nums[p] with nums[r]
            nums[p], nums[r] = nums[r], nums[p]

            # Call recursively for left and right parts, and exact match
            if k < p: return quickSelect(l, p - 1)
            elif k > p: return quickSelect(p + 1, r)
            else: return nums[p]

        # Initial call to quickSelect 
        return quickSelect(0, len(nums) - 1)