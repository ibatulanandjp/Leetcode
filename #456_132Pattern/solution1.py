# Method: Use stack and find array with minimum from left
# Then find other 2 numbers traversing in reverse order
# TC: O(n)
# SC: O(n)
from typing import List


class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        n = len(nums)
        # Create a list of minimum from left
        minFromLeft = [nums[0]]
        for i in range(1, n):
            minFromLeft.append(min(minFromLeft[i-1], nums[i]))

        # Use stack and traverse in reverse, to find the other 2 numbers satisfying condition
        stack = []
        for j in range(n-1, -1, -1):
            # Only if current number is greater than minimum from left at that index
            if nums[j] > minFromLeft[j]:
                # Remove any number from stack, which is smaller than minFromLeft (at that index)
                while stack and stack[-1] <= minFromLeft[j]:
                    stack.pop()
                # If the stack top is less than current num, return TRUE
                if stack and stack[-1] < nums[j]:
                    return True
                # Push the current number to stack
                stack.append(nums[j])
        return False
