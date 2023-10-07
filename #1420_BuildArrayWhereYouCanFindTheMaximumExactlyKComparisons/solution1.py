# Method: Using Dynamic Programming (3d array)
# TC: O(n * m * k)
# SC: O(n * m * k)
class Solution:
    def numOfArrays(self, n: int, m: int, k: int) -> int:
        # If maximum element is less than k, no valid array can be formed
        if m < k:
            return 0

        # Initialize a 3D DP array to store intermediate results
        # dp[i][j][x] represents the number of arrays of length i+1, ending with element j+1,
        # and having exactly x comparisons (search_cost) made so far.
        dp = [[1] * m] + [[0] * m for _ in range(k - 1)]
        mod = 10**9 + 7  # Modulo value for handling large numbers

        # Iterate through the array elements
        for _ in range(n - 1):
            # Iterate through the number of comparisons made so far
            for i in range(k - 1, -1, -1):
                cur = 0  # Variable to store the cumulative sum
                # Iterate through the possible elements in the array
                for j in range(m):
                    # Calculate the new value for dp[i][j]
                    # Here, j + 1 represents the maximum element that can be placed at index i,
                    # and cur represents the cumulative sum of dp[i - 1][j]
                    dp[i][j] = (dp[i][j] * (j + 1) + cur) % mod
                    # Update the cumulative sum for the next iteration
                    if i:
                        cur = (cur + dp[i - 1][j]) % mod

        # Sum up the values of dp[-1] (having k comparisons made) to get the total number of valid arrays
        # Take modulo operation to handle large numbers and return the result
        return sum(dp[-1]) % mod