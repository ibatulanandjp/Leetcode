# Method: 2-pass to first go left to right, and then back,
# calculating the optimal candies comparing from the previous one.
# TC: O(n)
# SC: O(n)
from typing import List


class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        candies = [1] * n

        # Pass 1: Move from left-to-right, and calculate the candies comparing with the left's rating
        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                candies[i] = candies[i-1] + 1

        # Pass 2: Move from right-to-left, and calculate the optimal candies
        for i in range(n-2, -1, -1):
            if ratings[i] > ratings[i+1]:
                candies[i] = max(candies[i], candies[i+1] + 1)

        return sum(candies)
