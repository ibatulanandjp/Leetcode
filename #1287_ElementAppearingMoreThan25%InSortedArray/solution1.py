# Method: Check the N/4 Look-ahead 
# TC: O(n)
# SC: O(1)
from typing import List


class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        size = len(arr) // 4
        for i in range(len(arr)):
            if i + size in range(len(arr)) and arr[i] == arr[i + size]:
                return arr[i]