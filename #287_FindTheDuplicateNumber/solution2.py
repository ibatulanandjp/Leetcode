# Method: Use Floyd's Cycle Detection Algorithm (Slow and Fast Pointers)
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Detect the cycle (keep the fast at the end)
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the start of the cycle (Duplicate Number)
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow
