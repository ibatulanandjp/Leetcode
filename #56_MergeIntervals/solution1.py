# Method: Sort by the first element in the interval and merge intervals
# TC: O(n logn), for sorting and iterating through the list
# SC: O(n), for storing merged intervals
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Sort the list with first element
        intervals.sort(key =lambda x: x[0])
        merged = [intervals[0]]
        
        for start, end in intervals:
            # Update the last element of merged with max of (merged last element, interval last element) 
            if merged[-1][1] >= start:
                merged[-1][1] = max(merged[-1][1], end)
            # Append element if no overlap
            else:
                merged.append([start, end])
            
        return merged