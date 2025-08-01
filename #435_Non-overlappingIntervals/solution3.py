# Method: Greedy with sorting by start, 
# checking for overlap and choosing the interval with smaller end
# TC: O(n log n) for sorting, O(n) for the loop
# SC: O(1) for the result count
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[0])
        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start >= lastEnd:
                # Non-Overlap: just add it
                lastEnd = end
            else:
                # Overlap: remove and pick the one with smaller end
                res += 1
                lastEnd = min(lastEnd, end)

        return res
