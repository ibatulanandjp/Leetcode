# Approach: Use Hash table (Array) to count character occurrences
# TC: O(n), where n is the length of s (or t, since they are the same length)
# SC: O(1) - since the character set is fixed (lowercase English letters)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        char_count = [0] * 26
        for i in range(len(s)):
            char_count[ord(s[i]) - ord('a')] += 1
            char_count[ord(t[i]) - ord('a')] -= 1
        
        for value in char_count:
            if value != 0:
                return False
        return True