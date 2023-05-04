from typing import List


# Method: Greedy Approach
# Move from right to left, moving the "Goal" closer if that can be reached
# TC: O(n)
# SC: O(1)
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # Set the goal initially to the end
        goal = len(nums) - 1
    
        # From right to left
        for i in range(len(nums)-1, -1, -1):
            # If the goal can be reached, move the goal left (towards the beginning)
            if i + nums[i] >= goal:
                goal = i
        
        # Return true if the goal is at the beginning, else false        
        return True if goal==0 else False
                