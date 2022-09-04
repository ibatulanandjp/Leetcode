from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxDiff = 0
        left = 0
        right = 1

        while right < len(prices):
            diff = prices[right] - prices[left]
            # print(diff)
            if diff < 0:
                left = right
                right = right+1

            else:
                if maxDiff < diff:
                    maxDiff = diff
                right = right+1

        return maxDiff


sol = Solution()
res = sol.maxProfit([7, 1, 5, 3, 6, 4]) #5
# res = sol.maxProfit([7, 6, 4, 3, 1]) #0
print("Max:", res)
