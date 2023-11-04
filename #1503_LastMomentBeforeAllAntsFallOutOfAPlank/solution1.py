# Method: Calculate max for the left and right ants, considering that they can pass each other
# TC: O(m + n), where m is the lenght of left, and n is the length of right
# SC: O(1)
from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        max_distance = 0

        for i in right:
            max_distance = max(max_distance, n - i)
        
        for i in left:
            max_distance = max(max_distance, i)

        return max_distance
            