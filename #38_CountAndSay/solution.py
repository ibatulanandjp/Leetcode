from typing import List


class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        say = self.countAndSay(n-1)
        l = self.convertCharCountMap(say)
        s = self.convertCharCountString(l)
        return s

    def convertCharCountMap(self, s: str) -> List[List[int]]:
        charCountList = []
        i = 0
        while i < len(s):
            curr = [1, int(s[i])]
            j = i+1
            while j < len(s) and s[i] == s[j]:
                curr[0] += 1
                j += 1
            charCountList.append(curr)
            i += curr[0]

        return charCountList

    def convertCharCountString(self, charCountMap: List[List[int]]) -> str:
        charCountString = ""
        for i in charCountMap:
            for j in i:
                charCountString += str(j)

        return charCountString
