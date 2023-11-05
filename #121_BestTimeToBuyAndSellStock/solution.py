# Method: Use 2 pointers to calculate the max difference
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_diff = 0
        left, right = 0, 1
        
        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff < 0:
                left = right
            elif max_diff < diff:
                max_diff = diff
            right += 1
        return max_diff