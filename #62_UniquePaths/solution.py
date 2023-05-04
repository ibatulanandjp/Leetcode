# Method: Dynamic Programming
# Store unique paths from last row and col, i.e. "1" in matrix
# Go on adding from last to the first cell
# Return the value at (0,0)
# TC: O(m*n)
# SC: O(m*n)
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        matrix = []

        # Initialize the matrix with
        # 0s: every element
        # 1s: the last element of the row/col
        for r in range(m):
            row = []
            for c in range(n):
                if r == m-1 or c == n-1:
                    row.append(1)
                else:
                    row.append(0)
            matrix.append(row)

        # Traverse every row and col from the end (in opposite direction), and go on adding the values
        r = m-1
        while r >= 0:
            c = n-1
            while c >= 0:
                if matrix[r][c] == 0:
                    matrix[r][c] = matrix[r+1][c] + matrix[r][c+1]
                c -= 1
            r -= 1

        return matrix[0][0]
