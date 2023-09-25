# Method: Use hashmap to count character occurences and return the extra one from "t"
# TC: O(n), where n is the length of the string
# SC: O(n), for the hashmap
from collections import defaultdict


class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        char_map = defaultdict(int)

        for i in range(len(s)):
            char_map[s[i]] += 1

        for i in range(len(t)):
            if t[i] not in char_map or char_map[t[i]] == 0:
                return t[i]
            char_map[t[i]] -= 1
        return t[-1]
