from typing import List

# Method: Recursively convert the integer to charCountString using helper functions
class Solution:
    def countAndSay(self, n: int) -> str:
        if n == 1:
            return "1"

        say = self.countAndSay(n-1)
        l = self.convertToCharCountList(say)
        s = self.convertToCharCountString(l)
        return s

    # Function to convert integer to charCountList
    def convertToCharCountList(self, s: str) -> List[List[int]]:
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

    # Function to convert charCountList to charCountString
    def convertToCharCountString(self, charCountList: List[List[int]]) -> str:
        charCountString = ""
        for i in charCountList:
            for j in i:
                charCountString += str(j)

        return charCountString
