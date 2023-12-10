# Method: Transpose matrix
# TC: O(m*n)
# SC: O(m*n)
from typing import List


class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        ROW, COL = len(matrix), len(matrix[0])
        res = [[0] * ROW for _ in range(COL)]

        for r in range(ROW):
            for c in range(COL):
                res[c][r] = matrix[r][c]
        return res