# Method: Using sorting to sort the strings and compare character-by-character
# TC: O(nlogn), where n is the length of the string
# SC: O(1)
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        if not s:
            return t
        s1 = sorted(s)
        t1 = sorted(t)

        for i in range(len(s1)):
            if s1[i] != t1[i]:
                return t1[i]
        return t1[-1]
