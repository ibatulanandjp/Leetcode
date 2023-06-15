# Method: Expand around centre (Both odd & even length)
# TC: O(n^2)
# SC: O(n) -> to save the resultant longest palindromic substring
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ""

        for i in range(len(s)):
            # Odd length palindrome
            l, r = i, i
            s1 = self.expandAroundCenter(s, l, r)
            if len(s1) > len(res):
                res = s1

            # Even length palindrome
            l, r = i, i+1
            s2 = self.expandAroundCenter(s, l, r)
            if len(s2) > len(res):
                res = s2

        return res

    def expandAroundCenter(self, s: str, left: int, right: int) -> str:
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        # Return left+1 since left is decremented in the last step,
        # And right remains as is since it was already incremented and acts as the right bound (excluded)
        return s[left+1:right]
