from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        left = 0
        right = 1

        while right < len(prices):
            diff = prices[right] - prices[left]
            if diff >= 0:
                profit += diff
            left = right
            right = right+1
        return profit
