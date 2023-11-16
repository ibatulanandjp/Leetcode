# Method: Cantor's Diagonal Argument (A proof in set theory)
# Invert diagonal characters of each number to get the answer
# TC: O(n), since we iterate over n numbers once
# SC: O(1)
from typing import List


class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        ans = []
        for i in range(len(nums)):
            curr = nums[i][i]
            ans.append("1" if curr == "0" else "0") 

        return "".join(ans)
