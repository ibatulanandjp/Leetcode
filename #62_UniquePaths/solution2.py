# Method: Dynamic Programming (Shorter version of solution1)
# TC: O(m*n)
# SC: O(m*n)

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        grid = [[0 for i in range(n)] for j in range(m)]

        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                if i == m-1 or j == n-1:
                    grid[i][j] = 1
                    continue
                grid[i][j] = grid[i+1][j] + grid[i][j+1]

        return grid[0][0]
