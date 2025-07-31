# Method: Greedy approach to insert and merge intervals into newInterval with 3 cases
# TC: O(n), where n is the number of intervals
# SC: O(n) for the result list
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []

        for i in range(len(intervals)):
            # Larger intervals
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            # Smaller intervals
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            # Merge into newInterval
            else:
                newInterval = [min(newInterval[0], intervals[i][0]), max(newInterval[1], intervals[i][1])]

        res.append(newInterval)
        return res