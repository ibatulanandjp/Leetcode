# Method: Sum of row and col is same for all diagonal elements.
# Use this to group all diagonals in a hashmap, and then combine them into a list
# TC: O(n), where n is the total numbers in the list
# SC: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        groups = defaultdict(list)
        for r in range(len(nums)-1, -1, -1):
            for c in range(len(nums[r])):
                diagonal = r + c
                groups[diagonal].append(nums[r][c])

        res = []
        curr = 0
        while curr in groups:
            res.extend(groups[curr])
            curr += 1

        return res