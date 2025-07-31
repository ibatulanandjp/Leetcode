# Method: Merge intervals when conditions are met
# TC: O(n), where n is the number of intervals
# SC: O(1), otherwise O(n) for the result list
from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        res = []
        i = 0

        # Append all smaller intervals
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            res.append(intervals[i])
            i += 1

        # Merge the intervals
        while i < len(intervals) and newInterval[1] >= intervals[i][0]:
            newInterval[0] = min(newInterval[0], intervals[i][0])
            newInterval[1] = max(newInterval[1], intervals[i][1])
            i += 1
        res.append(newInterval)
    
        # Append the rest of the intervals
        while i < len(intervals):
            res.append(intervals[i])
            i += 1
        
        return res