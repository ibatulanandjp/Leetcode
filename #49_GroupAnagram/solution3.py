from typing import List
from collections import defaultdict

# Method:
# Use HashMap to store the <sorted_word>:[..., <word>] as key:value
# TC: O(m * nlogn) -> m is the number of words, and n is the average length of each word
# SC: O(m * n) -> m is the number of words, and n is the average length of each word
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # defaultdict to avoid keyerror edge case (automatically handled, if a new key:value pair is added)
        res = defaultdict(list)

        for word in strs:
            # Sort each word for the key
            sorted_word = "".join(sorted(word))
            # Append the word with the sorted_word as the key (i.e. <sorted_word>: [..., <word>])
            res[sorted_word].append(word)

        return list(res.values())
