# Method: Sort and merge intervals
# TC: O(n logn)
# SC: O(n), for sorting
from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        merged = []
        # Sort the list with first element
        intervals.sort(key =lambda x: x[0])
        
        for i in intervals:
            # Append if not present or last merged element is less than interval's first element
            if not merged or merged[-1][1] < i[0]:
                merged.append(i)
            # Update the last element of merged with max of (merged last element, interval last element) 
            else:
                merged[-1][1] = max(merged[-1][1], i[1])
            
        return merged