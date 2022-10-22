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
        # print(matrix)

        r = m-1

        while r >= 0:
            c = n-1
            while c >= 0:
                if matrix[r][c] == 0:
                    matrix[r][c] = matrix[r+1][c] + matrix[r][c+1]
                c -= 1
            r -= 1

        return matrix[0][0]
