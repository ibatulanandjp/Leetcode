# Method: Use Dynamic Programming, and find the size of largest divisible subset for each index
# Traverse in reverse, getting the resultant subset
# TC: O(n^2)
# SC: O(n)

from typing import List


class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        dp = [1] * n
        max_size, max_index = 1, 0

        # Iterate and create the dp array keeping the size of largest divisible subset till that index
        # Also maintain max_size and max_index
        for i in range(1, n):
            for j in range(i):
                if nums[i] % nums[j] == 0:
                    dp[i] = max(dp[i], dp[j] + 1)
                    if dp[i] > max_size:
                        max_size = dp[i]
                        max_index = i

        # Backtrack from the max_index till the beginning, checking the numbers and saving into subset result
        # Reduce max_size as you find the number and go back
        result = []
        num = nums[max_index]
        for i in range(max_index, -1, -1):
            if num % nums[i] == 0 and dp[i] == max_size:
                result.append((nums[i]))
                num = nums[i]
                max_size -= 1

        return result
