from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        is_col = False
                
        for i in range(len(matrix)):
            if matrix[i][0] == 0:
                is_col = True
            for j in range(1, len(matrix[i])):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0                  
        
        for i in range(1, len(matrix)):
            for j in range(1, len(matrix[i])):
                # if i in row or j in col:
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0
                
        
        # If the 1st row needs to be set to zero
        if matrix[0][0] == 0:
            for j in range(len(matrix[0])):
                matrix[0][j] = 0
                
        if is_col:
            for i in range(len(matrix)):
                matrix[i][0] = 0