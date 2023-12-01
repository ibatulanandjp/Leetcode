# Method: Concatenate the strings and compare
# TC: O(n * k)
# SC: O(n * k)
from typing import List


class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        return "".join(word1) == "".join(word2)