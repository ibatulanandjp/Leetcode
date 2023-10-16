# Method: Use mathematical method to calculate next value using previous value
# TC: O(n)
# SC: O(n)
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        res = [1]
        prev = 1
        for i in range(1, rowIndex + 1):
            next_val = prev * (rowIndex - i + 1) // i
            res.append(next_val)
            prev = next_val
        return res
