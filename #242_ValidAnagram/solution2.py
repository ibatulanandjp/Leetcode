# Approach: Use hashmap to count character occurrences
# TC: O(n+m), where n is the length of s and m is the length of t
# SC: O(1) - since the character set is fixed (lowercase English letters)
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count_s, count_t = {}, {}
        for i in range(len(s)):
            count_s[s[i]] = 1 + count_s.get(s[i], 0)
            count_t[t[i]] = 1 + count_t.get(t[i], 0)
        
        return count_s == count_t