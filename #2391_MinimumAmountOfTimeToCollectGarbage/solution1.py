# Method: Calculate Prefix sum, and add value at each type's last index to find the result 
# TC: O(n)
# SC: O(n)
from typing import List


class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        # Caculate Prefix Sum
        prefix = [0]
        curr = 0
        for time in travel:
            curr += time
            prefix.append(curr)

        # Calculate the last index of each garbage type & sum all with prefix sum
        res = 0
        mIndex, gIndex, pIndex = 0, 0, 0
        for i in range(len(garbage)):
            if "M" in garbage[i]:
                mIndex = i
            if "G" in garbage[i]:
                gIndex = i
            if "P" in garbage[i]:
                pIndex = i
            # Add the length of the garbage at the index, since we picking all is required
            res += len(garbage[i])

        res += prefix[mIndex] + prefix[gIndex] + prefix[pIndex]
        return res
