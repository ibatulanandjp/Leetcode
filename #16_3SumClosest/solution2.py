from typing import List

# Method: Sort, and use 2 pointers, comparing absolute 'diff'
# TC: O(n^2)
# SC: O(1) -> O(n): In case when sort() function uses O(n) space

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        closest_sum = float('inf')

        # Sort the numbers
        nums.sort()

        # Fixating the first element
        for i in range(len(nums) - 2):
            # 2 Pointers: left, right
            l, r = i + 1, len(nums) - 1

            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]

                # Update closest_sum by comparing the absolute difference
                if abs(target - three_sum) < abs(target - closest_sum):
                    closest_sum = three_sum
                
                if three_sum < target:
                    l += 1
                elif three_sum > target:
                    r -= 1
                else:
                    return three_sum
        return closest_sum