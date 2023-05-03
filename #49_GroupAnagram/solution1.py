from typing import List
from collections import defaultdict

# Method:
# Sort each string and store the sorted string with index in a Map.
# Use the Map to create the result list
# TC: O(m * nlogn) -> m for no. of strings, nlogn for sorting each string


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # A dictionary to store <sorted(str):List[index]> 
        # (defaultdict never raises a KeyError. It provides a default value for the key that does not exists.)
        dict = defaultdict(list)
        res = []

        # Go through all the strings, sort them and store index in a map/dict
        for i, s in enumerate(strs):
            sorted_string = ''.join(sorted(s))
            dict[sorted_string].append(i)

        # Transform the dict/map to a list
        for key in dict:
            curr = []
            for _index in dict[key]:
                curr.append(strs[_index])
            res.append(curr)

        return res


sol = Solution()
res = sol.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"])
print(res)
