# Method: Dynamic Programming (Space Optimized) using 1D array
# TC: O(m * n), where m is the number of rows and n is the number of columns
# SC: O(n), where n is the number of columns
class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [0] * n

        for i in range(m):
            newRow = [1] * n
            for j in range(n - 2, -1, -1):
                newRow[j] = newRow[j + 1] + row[j]
            row = newRow
        return row[0]