# Method: Calculate t=d/s and sort it, to count the monster by comparing every index with time it takes to reach
# TC: O(n logn), required for sorting
# SC: O(n), required for time array
from typing import List

class Solution:
    def eliminateMaximum(self, dist: List[int], speed: List[int]) -> int:
        time = [dist[i] / speed[i] for i in range(len(dist))]
        time.sort()

        count = 0
        for i in range(len(time)):
            if time[i] <= i:
                break
            count += 1
        return count