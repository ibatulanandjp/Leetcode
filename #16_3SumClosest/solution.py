from typing import List


# Method: Sort, and use 2 pointers to solve 2Sum, comparing absolute 'diff'
# TC: O(n^2)
# SC: O(1) -> O(n): In case when sort() function uses O(n) space
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        res = float('-inf')
        diff = float('inf')

        # Sort nums 
        nums.sort()

        # Fixating first element
        for i in range(len(nums)):

            # 2 Pointers: left, right
            l, r = i + 1, len(nums) - 1

            while l < r:
                # Calculate 3 sum
                threeSum = nums[i] + nums[l] + nums[r]

                if threeSum < target:
                    l += 1
                elif threeSum >= target:
                    r -= 1

                # If the "currDiff" is less than "diff", update diff and res
                currDiff = abs(target - threeSum)
                if currDiff < diff:
                    diff = currDiff
                    res = threeSum

        return res
                