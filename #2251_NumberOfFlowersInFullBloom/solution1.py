# Method: Use Binary Search to find startedBlooming and endedBlooming
# Add (startedBlooming - endedBlooming) to result
# TC: O((n + m) logn), where n is the length of flowers, and m is the length of people
# SC: O(n)
from typing import List
from bisect import bisect_right


class Solution:
    def fullBloomFlowers(self, flowers: List[List[int]], people: List[int]) -> List[int]:
        starts = []
        ends = []

        # Create starts and ends list with starting and ending indices separately
        for start, end in flowers:
            starts.append(start)
            ends.append(end + 1)

        # Sort them individually
        starts.sort()
        ends.sort()
        ans = []

        # Perform binary search to find the rightmost insertion index of person in start and ends list
        # Add the difference to the answer
        for person in people:
            i = bisect_right(starts, person)
            j = bisect_right(ends, person)
            ans.append(i - j)

        return ans
