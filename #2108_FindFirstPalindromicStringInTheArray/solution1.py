# Method: Traverse and return the first one found
# TC: O(n * m), where n is the size of words list, and m is the maximum size of the words
# SC: O(1)
from typing import List


class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.checkPalindrome(word):
                return word
        return ""

    def checkPalindrome(self, word: str) -> bool:
        l, r = 0, len(word) - 1
        while l <= r:
            if word[l] != word[r]:
                return False
            l += 1
            r -= 1
        return True
