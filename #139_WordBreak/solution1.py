# Method: Use DP (bottom-up) maintaining a boolean array
# if the substring s[i:len(w)] is found in the wordDict
# TC: O(n * m * t), where n: length of s, m: no. of words in wordDict, t: max length of any word in wordDict
# SC: O(n), where n: length of s
from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and w == s[i:i+len(w)]:
                    dp[i] = dp[i + len(w)]
                if dp[i]:
                    break
        return dp[0]