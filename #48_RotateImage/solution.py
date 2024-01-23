# Method: Reverse and transpose
# TC: O(n^2)
# SC: O(1)
from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # Step1: Reverse the matrix
        matrix[:] = matrix[::-1]

        n = len(matrix)
        for i in range(n):
            for j in range(n):

                # Step2: Transpose elements
                # Swap the elements, only for the half of the matrix
                # Doing it for all will swap twice, so we avoid that
                if i < j:
                    matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
