# Method: Greedy with sorting by end
# TC: O(n log n) for sorting, O(n) for the loop
# SC: O(1) for the result count
from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals.sort(key = lambda x: x[1])
        res = 0
        lastEnd = intervals[0][1]

        for start, end in intervals[1:]:
            if start < lastEnd:
                # Overlap: need to remove 1
                res += 1
            else:
                # Non-overlapping: just append
                lastEnd = end

        return res
