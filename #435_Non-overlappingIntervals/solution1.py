# Method: Greedy with sorting and checking 2 conditions
# check overlap and choose the interval with smaller end
# TC: O(n log n) for sorting, O(n) for the loop
# SC: O(n) for the result list
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = [intervals[0]]
        lastEnd = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < lastEnd:
                # Overlap: choose interval with smaller end
                if intervals[i][1] < lastEnd:
                    lastEnd = intervals[i][1]
                    res[-1] = intervals[i]
            else:
                # Non-overlapping: just append
                res.append(intervals[i])
                lastEnd = intervals[i][1]

        return len(intervals) - len(res)
