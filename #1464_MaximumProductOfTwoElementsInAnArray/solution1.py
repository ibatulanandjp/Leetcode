# Method: Find the max and second max element from the list
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        biggest, second_biggest = 0, 0

        for num in nums:
            if num > biggest:
                second_biggest, biggest = biggest, num
            else:
                second_biggest = max(second_biggest, num)

        return (biggest - 1) * (second_biggest - 1)
