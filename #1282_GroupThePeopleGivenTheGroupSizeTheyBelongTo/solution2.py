# Method: Use Hashmap (1 pass) to put people's id with same groupSize into buckets,
# and append to result if bucket size is equal to the length
# TC: O(n)
# SC: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        groups = defaultdict(list)
        result = []
        for i, n in enumerate(groupSizes):
            # Add the current id into the bucket
            groups[n].append(i)

            # If bucket size already equal to the size, append to result, and clear the bucket
            if len(groups[n]) == n:
                result.append(groups[n])
                groups[n] = []
        return result
