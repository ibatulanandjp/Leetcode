# Method: Simulate stack
# TC: O(n)
# SC: O(1), since we don't use any extra space apart from the resultant array
from typing import List


class Solution:
    def buildArray(self, target: List[int], n: int) -> List[str]:
        res = []
        ptr = 0
        for num in range(1, n+1):
            if ptr in range(len(target)):
                if num == target[ptr]:
                    res.append("Push")
                    ptr += 1
                else:
                    res.append("Push")
                    res.append("Pop")
            else:
                break

        return res