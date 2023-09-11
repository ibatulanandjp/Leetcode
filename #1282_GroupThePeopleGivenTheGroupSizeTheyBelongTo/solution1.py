# Method: Use Hashmap (2 pass) to put people's id with same groupSize into buckets, and then split each bucket into groups
# TC: O(n)
# SC: O(n)
from typing import List
from collections import defaultdict


class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:

        # Create bucket of groupSizes with people ids as list of values
        groups = defaultdict(list)
        for i, n in enumerate(groupSizes):
            groups[n].append(i)

        # Split the bucket into groups of key size
        result = []
        for key, val in groups.items():
            groups = []
            for i in range(len(val)):
                groups.append(val[i])
                if (i+1) % key == 0:
                    result.append(groups)
                    groups = []

        return result
