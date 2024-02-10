# Method: Expand around center for odd and even length palindromes, counting palindromic substrings
# TC: O(n^2)
# SC: O(n)
class Solution:
    def countSubstrings(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            count += self.expandAroundCenter(s, i, i)
            count += self.expandAroundCenter(s, i-1, i)
        return count
    
    def expandAroundCenter(self, s: str, l: int, r: int) -> int:
        ps_count = 0
        while l >= 0 and r < len(s) and s[l] == s[r]:
            ps_count += 1
            l -= 1
            r += 1
        return ps_count