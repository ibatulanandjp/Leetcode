# Method: Use Monotonic Deque
# TC: O(n)
# SC: O(n)
from typing import List
from collections import deque


class Solution:
    def constrainedSubsetSum(self, nums: List[int], k: int) -> int:
        queue = deque()
        dp = [0] * len(nums)

        for i in range(len(nums)):
            if queue and i - queue[0] > k:
                queue.popleft()

            dp[i] = (dp[queue[0]] if queue else 0) + nums[i]
            while queue and dp[i] > dp[queue[-1]]:
                queue.pop()

            if dp[i] > 0:
                queue.append(i)
        return max(dp)
