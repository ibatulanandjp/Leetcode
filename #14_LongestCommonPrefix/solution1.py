# Method: Use first string to compare with all the other strings character-by-character
# TC: O(nm), n = no of strings, m = string with minimum length
# SC: O(m)
from typing import List


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        for i in range(len(strs[0])):
            for s in strs:
                if i == len(s) or strs[0][i] != s[i]:
                    return res
            res += strs[0][i]
        return res
