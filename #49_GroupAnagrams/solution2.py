from typing import List
from collections import defaultdict

# Method:
# Use HashMap to store the <count[]:s> as key:value 
# TC: O(m * n) -> m for list of strings, and n for each characters (max) in the string
# SC: O(m * n) -> m for list of strings, and n for each characters (max) in the string
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict to avoid keyerror edge case (automatically handled, if a new key:value pair is added)
        res = defaultdict(list)

        for s in strs:
            # List to store all the characters count of a string
            count = [0] * 26
            for ch in s:
                count[ord(ch) - ord("a")] += 1

            # Add <count: s> to the res dict
            # (converting to tuple since list can't be a "key" of a dict in python)
            res[tuple(count)].append(s)

        return res.values()