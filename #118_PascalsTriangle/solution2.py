from typing import List


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        res = [[1]]
        for i in range(numRows-1):
            temp = [1]
            for j in range(i):
                temp.append(res[i][j] + res[i][j+1])
            temp.append(1)
            res.append(temp)
        return res
