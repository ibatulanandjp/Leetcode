# Method: Sort the strings Lexicographically, and then compare the first and last string
# TC: O(nlogn * m), n = no of strings, m = string with minimum length
# SC: O(m)
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        strs.sort()
        first = strs[0]
        last = strs[-1]
        for i in range(min(len(first), len(last))):
            if first[i] != last[i]:
                return res
            res += first[i]
        return res
