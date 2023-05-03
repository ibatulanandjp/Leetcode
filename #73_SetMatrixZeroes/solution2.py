from typing import List

# TC: O(m*n)
# SC: O(1)
class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        ROWS, COLS = len(matrix), len(matrix[0])

        # Variable for the 1st element in the 1st column to check if it is "0"
        col_zero = False

        # Determine which rows and cols need to be "0", by keeping "0" in the 1st row and 1st col
        for r in range(ROWS):
            for c in range(COLS):
                if matrix[r][c] == 0:
                    matrix[r][0] = 0
                    # If 1st column, set col_zero
                    if c == 0:
                        col_zero = True
                    else:
                        matrix[0][c] = 0
                        
                        
        # Set the rows and cols to "0" (Skip the 1st row and col)
        for r in range(1, ROWS):
            for c in range(1, COLS):
                if matrix[r][0] == 0 or matrix[0][c] == 0:
                    matrix[r][c] = 0

        # If the 1st row needs to be set to "0"
        if matrix[0][0] == 0:
            for c in range(COLS):
                matrix[0][c] = 0

        # If the 1st col needs to be set to "0"
        if col_zero:
            for r in range(ROWS):
                matrix[r][0] = 0
