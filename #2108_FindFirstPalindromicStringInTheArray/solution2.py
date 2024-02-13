# Method: Traverse and return the first one found
# TC: O(n * m), where n is the size of words list, and m is the maximum size of the words
# SC: O(1)
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""
