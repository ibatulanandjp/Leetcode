# Method: Use sliding window with hashmap to track character frequencies
# and use frequency counts to determine when a valid window is found.
# TC: O(n + m), where n is the length of s and m is the length of t.
# SC: O(m), where m is the length of t for the hashmap.
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""

        res = ""
        min_window = float('inf')

        req_freq = {}
        for i in range(len(t)):
            req_freq[t[i]] = req_freq.get(t[i], 0) + 1
        req_len = len(req_freq)

        curr_freq = {}
        curr_len = 0
        l = 0
        for r in range(len(s)):
            curr_freq[s[r]] = curr_freq.get(s[r], 0) + 1

            if s[r] in req_freq and curr_freq[s[r]] == req_freq[s[r]]:
                curr_len += 1

            while curr_len == req_len:
                if (r - l + 1) < min_window:
                    min_window = r - l + 1
                    res = s[l:r+1]
                
                curr_freq[s[l]] -= 1
                if s[l] in req_freq and curr_freq[s[l]] < req_freq[s[l]]:
                    curr_len -= 1
                l += 1

        return res