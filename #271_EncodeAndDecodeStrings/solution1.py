
# Method:
# Use - len(str) + '#' + str - for encoding
# TC: O(m), where m is the sum of the lengths of all strings
# SC: O(m + n), where m is the sum of the lengths of all strings and n is the number of strings
from typing import List


class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + '#' + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s): 
            j = i
            while s[j] != '#':
                j += 1
            s_len = int(s[i:j])
            i = j + 1
            j = i + s_len
            res.append(s[i:j])
            i = j
        return res