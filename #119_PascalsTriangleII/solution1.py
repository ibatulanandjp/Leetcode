# Method: Append initial and last '1' and compute the elements in between using previous row
# TC: O(n^2)
# SC: O(n^2)
from typing import List


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        pascal = [[1]]
        for i in range(rowIndex):
            row = [1]
            for j in range(i):
                row.append(pascal[i][j] + pascal[i][j+1])
            row.append(1)
            pascal.append(row)
        return pascal[-1]
