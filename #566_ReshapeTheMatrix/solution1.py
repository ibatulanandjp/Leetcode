'''
[Method]: Array traversal and matrix manipulation
'''

from typing import List


class Solution:
    def reshapeTheMatrix(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:

        # Define the reshaped matrix
        res: List[List[int]] = [[0]*c for _ in range(r)]
        r1 = c1 = 0

        # Return the original matrix if size is different
        if r*c != len(mat)*len(mat[0]):
            return mat

        # For each element in mat
        for i in range(0, len(mat)):
            for j in range(0, len(mat[i])):

                res[r1][c1] = mat[i][j]

                # Increase row if end of the column
                if c1 == c-1:
                    r1 += 1
                    c1 = 0

                # Else increase the column
                else:
                    c1 += 1

        return res


sol = Solution()
res = sol.reshapeTheMatrix([[1, 2], [3, 4]], 1, 4)
# res = sol.reshapeTheMatrix([[1, 2], [3, 4]], 4, 1)
print(res)
