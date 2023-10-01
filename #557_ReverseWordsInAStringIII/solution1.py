# Method: Two-pointers to track each words, and reverse one-by-one
# TC: O(n), where n is the length of the string s
# SC: O(n)
class Solution:
    def reverseWords(self, s: str) -> str:
        res = ""

        l = 0
        for r, ch in enumerate(s):
            if ch == " ":
                curr_str = s[l:r]
                res += curr_str[::-1] + " "
                l = r + 1
            elif r == len(s)-1:
                curr_str = s[l:r+1]
                res += curr_str[::-1]

        return res
