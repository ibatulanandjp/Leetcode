# Method: Calculate max from max(left) and n-min(right)
# TC: O(m + n), where m is the lenght of left, and n is the length of right
# SC: O(1)
from typing import List


class Solution:
    def getLastMoment(self, n: int, left: List[int], right: List[int]) -> int:
        return max(max(left, default=0), n - min(right, default=n))
            